from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout


class TicTacModel:

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(32, input_dim=9, activation='relu'))
        self.model.add(Dropout(0.4))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(9, activation='sigmoid'))
        self.model.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train, epochs=1)

    def predict(self, state):
        return self.model.predict(state)

