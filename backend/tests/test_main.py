import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import hello

def test_hello():
    hello_str = hello.say_hello()
    assert hello_str == 'hello!'
