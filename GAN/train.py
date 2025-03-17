import tensorflow as tf
from GAN.gan import Pix2PixGAN
from GAN.dataloader import DataLoader

def train(epochs=50, batch_size=16):
    data_loader = DataLoader("train_layouts/", "train_masks/")
    layouts, masks = data_loader.load_images()

    dataset = tf.data.Dataset.from_tensor_slices((layouts, masks)).batch(batch_size)

    gan = Pix2PixGAN()
    gan.compile(gen_optimizer=tf.keras.optimizers.Adam(2e-4, beta_1=0.5),
                disc_optimizer=tf.keras.optimizers.Adam(2e-4, beta_1=0.5))

    gan.fit(dataset, epochs=epochs)

if __name__ == "__main__":
    train()
