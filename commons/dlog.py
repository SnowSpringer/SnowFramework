# 封装日志输出到文件，日志输出到控制台
import logging
import os


class SnowLog():
    #输入到文件，需要传递level等级，文件名
    def snowFileLog(self,level,filename):
        self.logger = logging.getLogger()
        # 进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not self.logger.handlers:
            self.logger.setLevel(level)

            log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
            formatter = logging.Formatter(log_format)
            self.handler = logging.FileHandler(filename)
            self.handler.setLevel(level)
            self.handler.setFormatter(formatter)
            self.logger.addHandler(self.handler)

    #输出到控制台,只需传递过去level
    def snowConsoleLog(self,level):
        self.logger = logging.getLogger()
        # 进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not self.logger.handlers:
            self.logger.setLevel(level)

            log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
            formatter = logging.Formatter(log_format)
            self.handler = logging.StreamHandler()
            self.handler.setLevel(level)
            self.handler.setFormatter(formatter)
            self.logger.addHandler(self.handler)



    def snowError(self,message):
        self.logger.error(message)


    def snowWarn(self,message):
        self.logger.warn(message)


    def snowInfo(self,meassage,*var):
        self.logger.info(meassage,vars(*var))






# 问题： 发现之前 封装的日志，放到接口框架请求中，一个请求，同一条返回日志记录，会重复记录四五遍
# 找到问题： 只增加handler ，没有移除。 本来是在最后 又定义了一个移除方法， 每个调用方法调一下移除。 但是发现不好用，重复代码有些多
# 解决： 在输出封装方法中，增加一个判断  if not self.logger.handlers ： 如果logger.handlers列表为空，则添加，否则，直接去写日志；这样handlers 不会多次添加

# 问题：想要print 正常输出内容，可以使用日志输出。warning， erroring 是错误才输出。默认warning 以上级别内容才输出
# 找到方法：logging 有五种级别。
# DEBUG	详细信息，通常仅在Debug时使用。
# INFO	程序正常运行时输出的信息。
# WARNING	表示有些预期之外的情况发生，或者在将来可能发生什么情况。程序依然能按照预期运行。
# ERROR	因为一些严重的问题，程序的某些功能无法使用了。
# CRITICAL	发生了严重的错误，程序已经无法运行。
# 可以设置level级别为info， 这样正常 输出内容即可输出