import sys
import cv2
from pprint import pprint
import numpy as np


# sys.path.insert(0, '/home/sparsha/ProjectWork/gitprojects/GeneticAlgorithmLibrary/')
sys.path.insert(0, "C:/Users/V/Downloads/Compressed/Genetic-Algorithm-In-Python-master")

from GeneticUtility import GeneticUtility
from Config import Config

# Define fitness function
def fitnessFunction(chromosome):
    fitness = 0
    for i in range(0, len(imageFlattened)):
        fitness += pow((imageFlattened[i] - chromosome.genes[i]), 2)

    return fitness    

# Read example image
# image = cv2.imread('/home/sparsha/ProjectWork/gitprojects/GeneticAlgorithmLibrary/Examples/s.jpg', 0)
image = cv2.imread('C:/Users/V/Downloads/Compressed/Genetic-Algorithm-In-Python-master/Examples/s.jpg', 0)

# Convert Image to List
imageFlattened = image.flatten().tolist()


# Convert 255's to 1 and rest to 0
# This is done in order to create binary image
for i in range(0, len(imageFlattened)):
    if imageFlattened[i] == 255:
        imageFlattened[i] = 1
    else:
        imageFlattened[i] = 0

image = np.reshape(imageFlattened, (20, 20)) * 255.0

# Step Executor Function
# Called after Each Generation for Any Action That the Programmer might want to execute
# Here we use this method to show the formed image at each step
from skimage.metrics import structural_similarity as ssim
def stepExecutor(generationNumber, bestIndividual):
    bestIndividual = np.array(bestIndividual.genes)
    bestIndividual = bestIndividual * 255.0
    bestIndividual = np.reshape(bestIndividual, (20, 20))
    bestIndividual = cv2.resize(bestIndividual, (200, 200))
    
    # Tính toán SSIM
    ssim_value = ssim(cv2.resize(image, (200, 200)), bestIndividual, data_range=bestIndividual.max() - bestIndividual.min())

    # Hiển thị kết quả SSIM
    print(f"Generation {generationNumber}, SSIM: {ssim_value}")

    # Show original Image and Formed Image at each step
    cv2.imshow("original Image", cv2.resize(image, (200, 200)))
    cv2.imshow("formed image", bestIndividual)
    key = cv2.waitKey(1)


# util = GeneticUtility(Config())
util = GeneticUtility()

x = util.simulateEvolution(300, fitnessFunction, stepExecution = stepExecutor)
x = np.array(x.genes)
x = x * 255.0
x = np.reshape(x, (20, 20))
cv2.imshow("formed image", x)
cv2.waitKey(0)





