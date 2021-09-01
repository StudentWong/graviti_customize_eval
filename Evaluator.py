import numpy as np

class Evaluator:
    def __init__(self):
        self.cnt = 0
        """
        You can initialize your model here
        """
        self.result = []
        ...
    def evaluate_one_data(self, input_source: dict, input_target: dict) -> dict:
        self.cnt = self.cnt + 0.5
        dict_ret = {
                'overall': {
                    'float_file_metric': self.cnt,
                }
        }
        self.result = self.result + [self.cnt]
        return dict_ret

    def get_result(self) -> dict:
        r = np.array(self.result)
        r_float = float(r.mean())
        dict_ret = {
            'overall': {
                'float_file_metric': r_float,
            }
        }
        return dict_ret

