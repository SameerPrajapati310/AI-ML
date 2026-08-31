from abc import ABC, abstractmethod


# 1. Base class defining the template method
class ModelTrainer(ABC):

    # Template method
    # Subclasses should not change this sequence
    def train_pipeline(self, data_path):

        self.load_data(data_path)
        self.preprocess_data()
        self.train_model()       # subclass-specific
        self.evaluate_model()    # subclass-specific
        self.save_model()        # subclass-specific or default

    # Common step
    def load_data(self, path):
        print(f"[Common] Loading dataset from {path}")
        # e.g. read CSV, images, etc.

    # Common step, but can be overridden
    def preprocess_data(self):
        print("[Common] Splitting into train/test and normalizing")

    # Subclass MUST implement
    @abstractmethod
    def train_model(self):
        pass

    # Subclass MUST implement
    @abstractmethod
    def evaluate_model(self):
        pass

    # Default implementation
    # Subclass can override if needed
    def save_model(self):
        print("[Common] Saving model to disk as default format")


# 2. Concrete subclass: Neural Network
class NeuralNetworkTrainer(ModelTrainer):

    def train_model(self):
        print("[NeuralNet] Training Neural Network for 100 epochs")
        # pseudo-code:
        # forward pass
        # backward pass
        # gradient descent

    def evaluate_model(self):
        print("[NeuralNet] Evaluating accuracy and loss on validation set")

    def save_model(self):
        print("[NeuralNet] Serializing network weights to .h5 file")


# 3. Concrete subclass: Decision Tree
class DecisionTreeTrainer(ModelTrainer):

    # Uses default preprocess_data()

    def train_model(self):
        print("[DecisionTree] Building decision tree with max_depth=5")
        # pseudo-code:
        # recursive splitting on features

    def evaluate_model(self):
        print(
            "[DecisionTree] Computing classification report "
            "(precision/recall)"
        )

    # Uses default save_model()


# 4. Usage
if __name__ == "__main__":

    print("=== Neural Network Training ===")

    nn_trainer = NeuralNetworkTrainer()
    nn_trainer.train_pipeline("data/images/")

    print("\n=== Decision Tree Training ===")

    dt_trainer = DecisionTreeTrainer()
    dt_trainer.train_pipeline("data/iris.csv")