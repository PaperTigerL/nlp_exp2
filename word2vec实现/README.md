# word2vec实现
数据集为'dataset/news.txt'，先进行数据预处理得到分词后的文件：
~~~python
python dataprocess.py
~~~~
得到cutdata.txt，再利用word2vec模型进行词嵌入：
~~~python
python train.py
~~~
得到word_embedding.txt文件，最后可测试效果：
~~~python 
python test.py
~~~

datasave文件夹已经包含经处理过后的cutdata_prepare.txt和word_embedding_pretrained.txt，可直接用来测试

