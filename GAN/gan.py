from GAN import generator
from GAN import discriminator

class GAN:
    m_generator = None
    m_discriminator = None
    
    def __init__(self):
        m_generator = generator.Generator()
        m_discriminator = discriminator.Discriminator()
        pass