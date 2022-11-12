import platform,psutil
from agent.lib.logger import Logger
class System_Info:
    def __init__(self):
        self.net=psutil.net_io_counters()
        self.io=psutil.disk_partitions()
        self.logger=Logger()

        self.info_based={}
        self.info_device={}

    def based_info(self):#静态信息初始化
        #self.logger.info("正在获取系统信息")
        self.system=str(platform.platform())#系统信息
        self.processor=str(platform.processor())#处理器信息
        self.system_v=str(platform.system())#是windows 还是 linux
        self.cpu_count=int(psutil.cpu_count(logical=False))#cpu物理数
        self.cpu_count_logical=int(psutil.cpu_count())#cpu逻辑数
        self.mem_gb = float(format(psutil.virtual_memory().total / 1024 / 1024 / 1024, '.1f'))#内存数gb
        self.mem_mb = float(format(psutil.virtual_memory().total / 1024 / 1024, '.1f'))#内存数mb

    def device_info(self):
        #self.logger.info("正在获取硬件使用信息")
        self.cpu_usage=float(psutil.cpu_percent(interval=0.1))

        self.bytes_sent = str('{0:.2f} Mb'.format(self.net.bytes_recv / 1024 / 1024))#网络出流量
        self.bytes_rcvd = str('{0:.2f} Mb'.format(self.net.bytes_sent / 1024 / 1024))#网络进流量

        self.mem_used=float(format(psutil.virtual_memory().used / 1024 / 1024, '.1f'))
        self.get_disk_info()

    def get_disk_info(self):
        self.total_disk = 0  # 单位g
        self.used_disk = 0
        self.free_disk = 0
        for i in self.io:
            diskinfo=psutil.disk_usage(str(i.device))
            self.total_disk+=float(format(diskinfo.total/(1024.0 * 1024.0 * 1024.0),".1f"))
            self.used_disk+=float(format(diskinfo.used/(1024.0 * 1024.0 * 1024.0),".1f"))
            self.free_disk+=float(format(diskinfo.free/(1024.0 * 1024.0 * 1024.0),".1f"))

    def return_info(self,mode="based"):
        if(mode=="based"):
            self.based_info()
            self.info_based['system']=self.system
            self.info_based['processor'] = self.processor
            self.info_based['system_v'] = self.system_v
            self.info_based['cpu_count'] = self.cpu_count
            self.info_based['cpu_count_logical'] = self.cpu_count_logical
            self.info_based['mem_gb'] = self.mem_gb
            self.info_based['mem_mb'] = self.mem_mb
            return self.info_based
        elif mode=="device":
            self.device_info()
            self.info_device['cpu_usage']=self.cpu_usage
            self.info_device['bytes_sent'] = self.bytes_sent
            self.info_device['bytes_rcvd'] = self.bytes_rcvd
            self.info_device['total_disk'] = self.total_disk
            self.info_device['used_disk'] = self.used_disk
            self.info_device['free_disk'] = self.free_disk
            self.info_device['mem_used'] = self.mem_used
            return self.info_device