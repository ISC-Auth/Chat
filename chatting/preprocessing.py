import json
import numpy as np
from scipy.spatial.distance import cosine


class GestureFeatureExtractor:
    def __init__(self):
        self.selected_feature = ['average_velocity','average_size','average_prs']
        self.prefixes = ['total','head_n','tail_n']
        self.n = 5
    
    def extract(self,slide):
        self.preprocessing_array(slide)
        return self.__do_extract()

    def __orientation(self,x0,y0,x1,y1): 
        return 1 - cosine(np.array([x1-x0,y1-y0]),np.array([1500-x0,0]))



    def __do_extract(self):
        '''
        slide => 字典数组
        形式： [{'X':'','Y':'','Xv':'','Yv':'','Prs':'','Size':''},{}]
        '''

        total_start_end_position = (self.X[0],self.Y[0],self.X[-1],self.Y[0])               # 0 1   2   3
        orientation = self.__orientation(self.X[0],self.Y[0],self.X[-1],self.Y[-1])         # 4


        total_average_velocity = (np.average(self.Xv[1:]),np.average(self.Yv[1:]))          # 6 7
        total_average_size = (np.average(self.sizes),)                                      # 8
        total_average_prs = (np.average(self.prs),)                                         # 9
        

        n = self.n

        head_n_average_velocity = (np.average(self.Xv[1:n]),np.average(self.Yv[1:n]))       #10  11
        head_n_average_size = (np.average(self.sizes[:n]),)                                 #12
        head_n_average_prs = (np.average(self.prs[:n]),)                                    #13

        tail_n_average_velocity = (np.average(self.Xv[-n:]),np.average(self.Yv[-n:]))       #14 15
        tail_n_average_size = (np.average(self.sizes[-n:]),)                                #16
        tail_n_average_prs = (np.average(self.prs[-n:]),)                                   #17

        features = []
        features.extend(total_start_end_position)
        features.append(orientation)
        features.append(self.X.shape[0])

        local = locals()
        for selected in self.selected_feature:
            for prefix in self.prefixes:
                f = local[prefix + '_' + selected]
                features.extend(f)

        return np.array(features)


    def preprocessing_array(self,slide):
        self.X = np.array([p["X"]  for p in slide])
        self.Y = np.array([p["Y"] for  p in slide])
        self.Xv = np.array([p["Xv"]  for p in slide])
        self.Yv = np.array([p["Yv"]  for p in slide])
        self.prs = np.array([p["Prs"]  for p in slide])
        self.sizes = np.array([p["Size"] for p in slide])

def normalize():
    pass
    

    



    
        

        
        

    