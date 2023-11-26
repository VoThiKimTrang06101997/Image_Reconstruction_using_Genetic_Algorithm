from Chromosome import Chromosome
from Config import Config

import random

class RouletteWheel(object):
    
    def __init__(self, chromosomes, config):
        self.chromosomes = chromosomes
        self.config = config
        self.__createCumulativeProbabilities__()
    
    def RouletteWheelSelection(self):
        # Select first chromosome
        random1 = random.uniform(0, 1)
        chromosome1 = None
        for chromosome in self.chromosomes:
            if random1 <= chromosome.endRange:
                chromosome1 = Chromosome(self.config)
                chromosome1.genes = chromosome.genes   # Tạo một bản sao của nhiễm sắc thể được chọn, bao gồm cả chuỗi gen của nó.
                break
        
        # Select second chromosome
        chromosome2 = None
        while True:
            random2 = random.uniform(0, 1)
            for chromosome in self.chromosomes:
                if random2 <= chromosome.endRange:
                    chromosome2 = Chromosome(self.config)
                    chromosome2.genes = chromosome.genes
                    
                    if chromosome1.genes != chromosome2.genes:
                        return chromosome1, chromosome2

    # Thiết lập các khoảng xác suất tích lũy cho mỗi nhiễm sắc thể, dựa trên độ thích nghi 
    #  Tạo ra một chuỗi các khoảng xác suất tích lũy cho mỗi nhiễm sắc thể. endRange của một nhiễm sắc thể càng lớn, khả năng nó được chọn trong quá trình lựa chọn roulette càng cao => Đảm bảo rằng nhiễm sắc thể có độ thích nghi cao (normalizedFitness cao hơn) sẽ có cơ hội lớn hơn trong việc được chọn so với những nhiễm sắc thể có độ thích nghi thấp.)
    def __createCumulativeProbabilities__(self):
        self.__calculateCumulativeSum__()
        self.__getNomalizedFitness__()
        currentSum = 0
        for chromosome in self.chromosomes:
            currentSum += chromosome.normalizedFitness
            chromosome.endRange = currentSum
    
    #  Tính tổng cộng của độ thích nghi (fitness) cho tất cả các nhiễm sắc thể trong quần thể.
    def __calculateCumulativeSum__(self):
        cumSum = 0
        for chromosome in self.chromosomes:
            cumSum += chromosome.fitness
        self.cumSum = cumSum
     
     #  Tính toán tổng cộng của độ thích nghi (fitness) cho tất cả các nhiễm sắc thể trong quần thể.
     #  normalizedFitness được tính cho mỗi nhiễm sắc thể, là tỷ lệ giữa độ thích nghi của nó so với tổng cộng (tính xác suất trung bình).
    def __getNomalizedFitness__(self):
        for chromosome in self.chromosomes:
            chromosome.normalizedFitness = chromosome.fitness / self.cumSum
