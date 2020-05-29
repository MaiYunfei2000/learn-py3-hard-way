# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab

########################################

import time
random.seed(0)

########################################

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        if self.getClearProb() >= random.random():
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        if self.maxBirthProb * (1 - popDensity) >= random.random():
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException

class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.getViruses())

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        # for each virus in existing viruses
        for virus in self.viruses.copy():
            # check and clear the virus
            if virus.doesClear():
                self.viruses.remove(virus)
        
        # caculate the population density with its definition
        popDensity = len(self.viruses) / self.getMaxPop()
        
        # for each virus in existing viruses
        for virus in self.viruses.copy():
            # reproduce new virus stochastically
            try:
                self.viruses.append(virus.reproduce(popDensity))
            except NoChildException:
                pass
        
        return len(self.viruses)


# # testing and debugging
# virus = SimpleVirus(1.0, 0.0)
# patient = Patient([virus], 100)
#
# print("-" * 50)
# print("* patient.getTotalPop()", patient.getTotalPop())
# print("* patient.getViruses()", patient.getViruses())
# print("-" * 50)
#
# for i in range(10):
#     patient.update()
#     print("patient.getTotalPop()", patient.getTotalPop())
#     print("patient.getViruses()", patient.getViruses())

#
# PROBLEM 2
#

import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    popMatrix = []
    
    for trial in range(numTrials):
        # initialization
        # timesteps = [] # later used for axis x
        population = [] # later used for axis y
        patient = Patient([SimpleVirus(maxBirthProb, clearProb)] * numViruses, maxPop)
        
        for timestep in range(300):
            patient.update()
            # timesteps.append(timestep)
            population.append(patient.getTotalPop())
        popMatrix.append(population)
        # print('-'*50, '\n', populationMatrix) # debug use
    
    avgPop = np.mean(popMatrix, 0)
    # print("avgPop", avgPop, "\ncheck list len", len(avgPop)) # debug use
    
    pylab.plot(list(avgPop), label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()

# simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)

#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        try:
            return self.getResistances()[drug]
        except KeyError:
            pass

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        # represent the virus' resistance to drugs in activeDrugs
        resistanceToActiveDrugs = [self.isResistantTo(drug) for drug in activeDrugs]
        # for drug in activeDrugs:
        #     # dual fail-safe but just redundant
        #     try:
        #         resistanceToActiveDrugs.append(self.isResistantTo(drug))
        #     except KeyError:
        #         pass
        
        # if the virus is resistant to all drugs in activeDrugs
        if all(resistanceToActiveDrugs):
            if self.maxBirthProb * (1 - popDensity) >= random.random():
                # specify the mutation of the resistance of the child
                resistancesOfChild = {}
                for drug in self.getResistances().keys():
                    if self.getMutProb() >= random.random():
                        resistancesOfChild[drug] = not self.resistances[drug]
                    else:
                        resistancesOfChild = self.resistances
                return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(),
                                   resistancesOfChild, self.getMutProb())
            else:
                raise NoChildException
        else:
            raise NoChildException


# virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
# for i in range(10):
#     print(virus.reproduce(0, []).getResistances())

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.activeDrugs = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.activeDrugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistPop = 0
        for virus in self.getViruses():
            if (drugResist != [] and
                    all([virus.isResistantTo(drug) for drug in drugResist])):
                resistPop += 1
        return resistPop

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        # for each virus in existing viruses
        for virus in self.viruses.copy():
            # check and clear the virus
            # print("virus in self.viruses.copy()", virus)
            if virus.doesClear():
                self.viruses.remove(virus)
        
        # caculate the population density with its definition
        popDensity = len(self.viruses) / self.getMaxPop()
        
        # for each virus in existing viruses
        for virus in self.viruses.copy():
            # reproduce new virus stochastically
            try:
                # print(virus.reproduce(popDensity, self.activeDrugs)) # debug use
                child = virus.reproduce(popDensity, self.getPrescriptions())
                # print("a virus", virus.resistances) # debug use
                # print("child of the virus", child.resistances) # debug use
                self.viruses.append(child)
                # print("Successfully Reproduce") # debug use
                # print("Patient's Viruses", self.getViruses(), self.viruses) # debug use
                # print([virus.resistances for virus in self.getViruses()]) # debug use
            except NoChildException:
                # print("NoChildException") # debug use
                pass
        
        return len(self.viruses)

# simulation and debugging

numViruses, maxPop, maxBirthProb, clearProb = 2, 50, 0.5, 0.0
resistances, mutProb, numTrials = {'guttagonol': False}, 0.5, 50

# initialization
population = []
resistPopulation = []
patient = TreatedPatient([ResistantVirus(maxBirthProb, clearProb, resistances,
                          mutProb)] * numViruses, maxPop)
                          
for i in range(50):
    print("i =", i) # debug use
    patient.update()
    print("resistant population", patient.getResistPop(['guttagonol']))
    time.sleep(0.1) # debug use
    
    
# why method getRestistPop acts up????