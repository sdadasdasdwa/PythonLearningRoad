

class Person:
    def __init__(self,attr,chrom_size,interval):
        self.attr = attr
        self.interval = interval
        self.chrom_size = chrom_size
        self.fitness = self.evaluate(self.map_into(attr[0]),self.map_into(attr[1]))
        # self.fitness = self.evaluate(attr[0],attr[1])
    def map_into(self,x):
        d = self.interval[1] - self.interval[0]
        n = float (2 ** self.chrom_size -1)
        return (self.interval[0] + x * d / n)
    def evaluate(self,x,y):# to compute the fitness
        n = lambda x, y: 6.452*(x + 0.125*y)*(math.cos(x) - math.cos(2*y))**2
        d = lambda x, y: math.sqrt(0.8 + (x - 4.2)**2 + 2*(y - 7)**2)
        func = lambda x, y: n (x, y)/d (x, y) + 3.226*y
        # func = lambda x, y: -(20+x**2+y**2-10*(math.cos(2*math.pi*x+2*math.pi*y)))
        return func (x, y)

import random
import math
import statistics

class Population:
    def __init__(self,max_num,capacity,mutation_rate,cross_rate,chrom_size):
        self.current_generation = []
        self.next_generation = []
        self.max_generations = max_num
        self.size = capacity
        self.mutation_rate = mutation_rate
        self.cross_rate = cross_rate
        self.chrom_size = chrom_size
        self.interval = (0,10)
        self.select_prob = []
        self.best = None
        size = 2**self.chrom_size - 1
        for i in range(capacity):
            x,y = random.randint(0,size),random.randint(0,size)
            one = Person((x,y),self.chrom_size,self.interval)

            self.current_generation.append(one)



    def generate_selectprob(self):
        prob = 0
        self.select_prob = []
        total = sum(p.fitness for p in self.current_generation)
        for each in self.current_generation:
            prob += each.fitness/total
            self.select_prob.append(prob)
    def select(self):
        t = random.random()
        i = next(i for i,p in enumerate(self.select_prob) if t < p)
        return self.current_generation[i]
    def cross(self,chrom1,chrom2):
        #now:swap only one part
        # to do:swap several part of chroms
        p = random.random()
        if chrom1!=chrom2 and p < self.cross_rate:
            pos = random.randint(0,self.chrom_size-1)
            mask1,mask2 = (2**self.chrom_size-1)<<pos,2**pos-1
            t1,t2 = chrom1&mask1,chrom2&mask1
            r1,r2 = chrom1&mask2,chrom2&mask2
            chrom1,chrom2 = t1+r2,t2+r1
        return chrom1,chrom2
    def mutate(self,chrom):
        p = random.random()
        if p<self.mutation_rate:
            pos =  random.randint(1,self.chrom_size)
            mask1 = 1<<(pos-1)
            chrom = chrom^mask1
        return chrom
    def evolve(self):
        self.generate_selectprob()
        num = 0
        while num < self.size:
            #cross
            indv1,indv2 = self.select(),self.select()
            indv1_x,indv2_x = self.cross(indv1.attr[0],indv2.attr[0])
            indv1_y,indv2_y = self.cross(indv1.attr[1],indv2.attr[1])
            #mutation
            tmp = [indv1_x,indv1_y,indv2_x,indv2_y]
            [indv1_x,indv1_y,indv2_x,indv2_y] = [self.mutate(u) for u in tmp]
            one = Person((indv1_x,indv1_y),self.chrom_size,self.interval)
            two =  Person((indv2_x,indv2_y),self.chrom_size,self.interval)
            self.next_generation.append(one)
            self.next_generation.append(two)
            num+=2
        self.current_generation = self.next_generation
        self.next_generation = []
    def run (self):
        for i in range (self.max_generations):
            self.evolve()
            _,_,self.best = max((p.fitness,i,p) for i,p in enumerate(self.current_generation))
            worest,i = min((p.fitness,i) for i,p in enumerate(self.current_generation))
            self.current_generation[i] = self.best
            print(self.best.fitness,statistics.mean(p.fitness for p in self.current_generation),worest,self.best.map_into(self.best.attr[0]),self.best.map_into(self.best.attr[1]))

print('50')
population = Population(150,150,0.3,0.8,50)
ans = population.run()
# a = Person((0.1568522358047586,-0.17042440166827877),1,(0,1))
# print(a.fitness)
