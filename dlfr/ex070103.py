##### 7.1.3 多输出模型


### 7-3 用函数式 API 实现一个三输出模型

from keras import layers
from keras import Input
from keras.models import Model

vocabulary_size = 50000
num_income_groups = 10

posts_input = Input(shape=(None,), dtype='int32', name='posts')
embedded_posts = layers.Embedding(vocabulary_size, 256)(posts_input)
x = layers.Conv1D(128, 5, activation='relu')(embedded_posts)
x = layers.MaxPooling1D(5)(x)
x = layers.Conv1D(256, 5, activation='relu')(x)
x = layers.Conv1D(256, 5, activation='relu')(x)
x = layers.MaxPooling1D(5)(x)
x = layers.Conv1D(256, 5, activation='relu')(x)
x = layers.Conv1D(256, 5, activation='relu')(x)
x = layers.Dense(128, activation='relu')(x)

## 注意，输出层都具有名称
age_prediction = layers.Dense(1, name='age')(x)
income_prediction = layers.Dense(num_income_groups,
                                 activation='softmax',
                                 name='income')(x)
gender_prediction = layers.Dense(1, activation='sigmoid', name='gender')(x)

model = Model(posts_input,
              [age_prediction, income_prediction, gender_prediction])


### 7-4 多输出模型的编译选项：多重损失

model.compile(optimizer='rmsprop',
              loss=['mse', 'categorical_crossentropy', 'binary_crossentropy'])

## 与上述写法等效（只有输出层都具有名称时才能采用这种写法）
model.compile(optimizer='rmsprop',
              loss={'age': 'mse',
                    'income': 'categorical_crossentropy',
                    'gender': 'binary_crossentropy'})


### 7-5 多输出模型的编译选项：损失加权

model.compile(optimizer='rmsprop',
              loss=['mse', 'categorical_crossentropy', 'binary_crossentropy'],
              loss_weights=[0.25, 1, 10.])
              
## 与上述写法等效（只有输出层都具有名称时才能采用这种写法）
model.compile(optimizer='rmsprop',
              loss={'age': 'mse',
                    'income': 'categorical_crossentropy',
                    'gender': 'binary_crossentropy'},
              loss_weights={'age': 0.25,
                            'income': 1,
                            'gender': 10.})

### 7-6 将数据输入到多输出模型中

## 假设 age_targets、income_targets 和 gender_targets 都是 Numpy 数组
model.fit(posts, [age_targets, income_targets, gender_targets],
         epochs=10, batch_size=64)

## 与上述写法等效（只有输出层都具有名称时才能采用这种写法）
model.fit(posts, {'age': age_targets, 
                  'income': income_targets, 
                  'gender': gender_targets},
         epochs=10, batch_size=64)