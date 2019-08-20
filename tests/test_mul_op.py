#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import numpy as np
from op_test import OpTest


class TestMulOp(OpTest):
    def setUp(self):
        self.op_type = 'mul'
        self.inputs = {
            'X': np.random.random((15, 4, 12, 10)).astype('float32'),
            'Y': np.random.random((30, 4, 4, 9)).astype('float32')
        }
        self.attrs = {'x_num_col_dims': 2, 'y_num_col_dims': 2}
        self.outputs = {'Out': np.zeros((1, 1))}

    def test_check_output(self):
        self.check_output()


if __name__ == '__main__':
    unittest.main()