# 吴巨-25311061-第二次人工智能编程作业

## 1. 任务拆解与 AI 协作策略

在编写代码之前，我将这个项目分解成 10 个步骤

步骤 1：创建仓库与本地初始化

步骤 2：定义 Student 类

步骤 3：定义 ExamSystem 类与静态方法

步骤 4：实现信息初始化与查找功能

步骤 5：实现随机点名功能

步骤 6：实现生成考场安排表功能

步骤 7：实现生成准考证目录与文件功能

步骤 8：检查异常处理

步骤 9：编写 README.md 报告

步骤 10：最终检查与提交

### 步骤 1

安装 git ，但是输入 git --version 发现报错，

![](images/imgs2.png)

question1: 如何解决 git 路径报错问题

answer1:![](images/img3.png)![](images/img4.png)
![](images/img5.png)![](images/img6.png)

设置成功后我配置了自己的 github 信息,

question2: 如何初始化git

answer2: ![](images/img1.png)

初始化完成 ![](images/img10.png)

### 步骤 2

之后我通过 prompt coding 节省时间

question3 and answer3:基于给出的步骤2，生成该步骤的代码

生成之后我加以理解并给出中文注释（代码在后续步骤中被部分修改，
因此注释贴图部分我将在最后给出）

完成之后我尝试把代码推送到仓库但是报错

question4:分析将代码推送到 github 仓库而报错的原因
![](images/img7.png)

answer4:![](images/img8.png) ![](images/img9.png)

完成之后我推送了步骤 2 的代码 

### 步骤 3-7

与步骤 2 一样使用 prompt coding 节省时间（其中 debug
部分在下面展示）

question3-7 and answer3-7:基于给出的步骤3-7，生成该步骤的代码
（实际操作过程是给出 5 个 prompt ，并且 debug 之后才进入下一步）

生成之后我加以理解并让 AI 迭代加上 try-expect 代码块（迭代过程在下面展示）
，同时给出中文注释

![](images/img11.png)
![](images/img12.png) ![](images/img13.png)
![](images/img14.png) ![](images/img15.png)


### 步骤 8

最后我将全部代码的异常处理部分完整检查一遍，并没有发现错误

![](images/img16.png)

### 步骤 9-10

README撰写完成后将该项目提交

## 2. 核心 prompt 迭代记录

步骤 3 一开始 AI 给出的代码不含 try-expect 代码块

question8 and answer8：用try-expect代码块处理潜在的异常，
并且在此基础上重新生成步骤 3 的代码

![](images/img17.png)

（完整代码会在下面给出）

## 3. debug 与异常处理记录

运行步骤 4 之后发现无法进行查找测试

![](images/img18.png)

此处进行利用 AI 进行 debug 以节省时间

question9 and answer9：步骤4 运行 main 文件后，
无法查找测试，请分析其中原因并给出解决方案

![](images/img19.png) ![](images/img20.png)

debug 成功

![](images/img21.png) ![](images/img27.png)

运行步骤 5 没发现表头行没剔除，
不过在后续步骤 6 及时发现并剔除

![](images/img22.png)

步骤 6 剔除表头行

![](images/img23.png)

此处因为知道 bug 在哪，所以人工 debug

![](images/img24.png) ![](images/img25.png)
![](images/img28.png) ![](images/img26.png)

debug 成功

运行步骤 7 之后发现属性异常

![](images/img29.png)

此处进行利用 AI 进行 debug 以节省时间

question9 and answer9：步骤7 运行 main 文件后，
出现属性异常，，请分析其中原因并给出解决方案

![](images/img30.png) ![](images/img31.png)
![](images/img32.png) ![](images/img33.png)

debug 成功

## 4. 人工代码审查

此处贴上所有代码（均有人工加上的中文注释）

![](images/img34.png)![](images/img35.png)
![](images/img36.png)![](images/img37.png)
![](images/img38.png)![](images/img39.png)
![](images/img40.png)![](images/img41.png)
![](images/img42.png)![](images/img43.png)
![](images/img44.png)
