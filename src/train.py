from src import generator


# Trains model and saves weights
def train(model, scale, batch_size, epochs): 
    training_generator = generator.DataGenerator(scale = scale, batch_size = batch_size, type = "train")
    
    
    model.fit_generator(generator = training_generator, epochs=epochs, verbose=1)

    # Save weights
    filepath = 'src/' + 'x' + str(scale) + 'bs' + str(batch_size) + 'epochs' + str(epochs) +  'weights.h5'
    model.save_weights(filepath)
    print("Weights saved at：" + filepath)