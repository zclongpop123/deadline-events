#========================================
#    author: hanjuntai
#      mail: hanjuntai@yeah.net
#      time: 13/05/2020
#========================================
from System import *
from Deadline.Events import *
from Deadline.Scripting import *
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def GetDeadlineEventListener():
    return MayaEnvListener()


def CleanupDeadlineEventListener(eventListener):
    return eventListener.Cleanup()


class MayaEnvListener(DeadlineEventListener):
    '''
    '''

    def __init__(self):
        '''
        '''
        self.OnJobSubmittedCallback += self.OnJobSubmitted



    def Cleanup(self):
        '''
        '''
        del self.OnJobSubmittedCallback


    def OnJobSubmitted(self, job):
        '''
        '''
        if job.JobPlugin == 'MayaCmd' or job.JobPlugin == 'MayaBatch':
            job.SetJobEnvironmentKeyValue('ARNOLD_PLUGIN_PATH',  '//192.168.15.15/pipeline/packages/CryptomatteArnold/ai5.0.1.0/bin;//oct.ds.com/TD/Tools/OCT_Toolkits/DCC_TOOLS/maya_plugins/2017')
            job.SetJobEnvironmentKeyValue('MTOA_TEMPLATES_PATH', '//192.168.15.15/pipeline/packages/CryptomatteArnold/ai5.0.1.0/ae')
            job.SetJobEnvironmentKeyValue('MAYA_CUSTOM_TEMPLATE_PATH', '//192.168.15.15/pipeline/packages/CryptomatteArnold/ai5.0.1.0/aexml')
            job.SetJobEnvironmentKeyValue('solidangle_LICENSE', '5053@lic.ds.com')
            RepositoryUtils.SaveJob(job)
