#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Sat Mar 28 08:19:51 2020
#========================================
import re, requests
from datetime import datetime
from Deadline.Events import * 
from Deadline.Scripting import *
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def GetDeadlineEventListener():
    return ShutdownEvent()


def CleanupDeadlineEventListener(deadlinePlugin):
    deadlinePlugin.Cleanup()


class ShutdownEvent(DeadlineEventListener):
    '''
    '''

    def __init__(self):
        '''
        '''
        self.OnJobFinishedCallback += self.OnJobFinished
        self.OnJobFailedCallback   += self.OnJobFinished



    def Cleanup(self):
        '''
        '''
        del self.OnJobFinishedCallback
        del self.OnJobFailedCallback



    def OnJobFinished(self, job):
        '''
        '''
        work_start_time = self.GetIntegerConfigEntryWithDefault('WorkTimeStart', 9)
        work_end_time   = self.GetIntegerConfigEntryWithDefault('WorkTimeEnd',  19)

        now = datetime.now()
        if now.hour in range(work_start_time, work_end_time):
            self.LogInfo('Day work time can not close machine !')
            return


        host = self.GetConfigEntryWithDefault('WebServiceHost', 'localhost')
        port = self.GetIntegerConfigEntryWithDefault('WebServicePort', 8082)

        jobs = requests.get('http://{0}:{1}/api/jobs'.format(host, port))
        for job in jobs.json():
            if job.get('QueuedChunks',    0) > 0:
                self.LogInfo('Other task in Queued, can not shutdown slave...')
                return

            if job.get('RenderingChunks', 0) > 0:
                self.LogInfo('Other task is Rendering, can not shutdown slave...')
                return

        self.LogInfo('Start to close slaves...')
        slaves = requests.get('http://{0}:{1}/api/slaves?Data=infosettings'.format(host, port))
        for slave in  slaves.json():
            if not re.match('F7|render|Renderfarm', slave['Info']['Host'], re.I):
                continue
            SlaveUtils.SendRemoteCommand(slave['Info']['IP'], 'ShutdownMachine')
