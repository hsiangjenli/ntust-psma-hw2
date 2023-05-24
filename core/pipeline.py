import pandas as pd

class ScoreFuncPipeline:
    def __init__(self, **socre_func: dict) -> None:
        """
        **Score Function Pipeline**
        ---------------------------

        > A pipeline for calculating the score of the graph

        Parameters
        ----------
        **socre_func : dict
            The key is the name of the score function, and the value is the score function.
        
        Example
        -------
        ```python

        def cal_neighbors_size(row, **kwargs):
            return kwargs['graph'].get_neighbors_size(row["node1"])
        
        def cal_common_neighbors(row, **kwargs):
            return kwargs['graph'].common_neighbors(row["node1"], row["node2"])
            
        socre_func = {
            "out": cal_neighbors_size,
            "common_neighbors": cal_common_neighbors
        }

        pipeline = ScoreFuncPipeline(**socre_func)
        sc_train, sc_test = pipeline.transform(graph=graph, df_train=train, df_test=test)
        
        ```
        """
        self.score_func = socre_func
    
    def transform(self, graph: dict, **kwargs) -> list:
        """

        Parameters
        ----------
        graph : dict
            _description_

        **kwargs : dict  
            1. If the key of kwargs starts with `df_`, it will be considered as a dataframe, and will be transformed by the score function.  
            1. Otherwise, it will be passed as a parameter to the score function.
        

        Returns
        -------
        list[pd.DataFrame]
            return a list of transformed dataframe.
        """

        kwargs.update({"graph": graph})

        transformed_dfs = []
        
        for name, df in kwargs.items():
            if name.startswith("df_"):
                transformed_dfs.append(self.cal_func_score(df=df, **kwargs))
        
        return transformed_dfs
    
    def cal_func_score(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df = df.copy()
        
        for func_name, func in self.score_func.items():
            df[func_name] = df.apply(func, axis=1, **kwargs)
        
        return df