#Importing prometheus library
from prometheus_client import Info,Gauge,Enum

#---------#---------#---------#---------#---------#
# Orchestrator Metrics
#---------#---------#---------#---------#---------#

uptime = Info('uptime', 'silverpeak orchestrator uptime',['orchName'])
release = Info('release', 'silverpeak orchestrator release version',['orchName'])
platform = Info('platform', 'silverpeak orchestrator platform',['orchName'])
numActiveUsers = Gauge('numActiveUsers', 'number of active users logged in',['orchName'])
activeAlarms = Gauge('activeAlarms', 'summary of active alarms for Orchestrator and all appliances',['orchName','severity'])
totalAppliances = Gauge('totalAppliances', 'number of total appliances in your orchestrator',['orchName'])
licenseNumMini  = Gauge('licenseNumMini', 'number of mini licenses',['orchName'])
licenseNumBase  = Gauge('licenseNumBase', 'number of base licenses',['orchName'])
licenseNumBoost  = Gauge('licenseNumBoost', 'number of boost licenses',['orchName'])
licenseNumPlus  = Gauge('licenseNumPlus', 'number of plus licenses',['orchName'])
licenseNumTier20M = Gauge('licenseNumTier20M', 'number of 20M licenses',['orchName'])
licenseNumTier50M = Gauge('licenseNumTier50M', 'number of 50M licenses',['orchName'])
licenseNumTier100M = Gauge('licenseNumTier100M', 'number of 100M licenses',['orchName'])
licenseNumTier200M = Gauge('licenseNumTier200M', 'number of 200M licenses',['orchName'])
licenseNumTier500M = Gauge('licenseNumTier500M', 'number of 500M licenses',['orchName'])
licenseNumTier1G = Gauge('licenseNumTier1G', 'number of 1G licenses',['orchName'])
licenseNumTier2G = Gauge('licenseNumTier2G', 'number of 2G licenses',['orchName'])
licenseNumTierUM = Gauge('licenseNumTierUM', 'number of Unlimited licenses',['orchName'])
totalOverlays = Gauge('totalOverlays', 'number of overlays configured',['orchName'])
totalRegions = Gauge('totalRegions', 'number of regions configured',['orchName'])
totalSaasApps = Gauge('totalSaasApps', 'list of unique SaaS applications in the internet services database',['orchName'])
totalAppDefinition = Gauge('totalAppDefinition', 'count for application definition data for Address Map from Cloud Portal',['orchName'])
totalOrchSaasApps = Gauge('totalOrchSaasApps', 'count of internet services defined on Orchestrator',['orchName'])
orchPortalStatus = Enum('orchPortalStatus', 'current connectivity status between Orchestrator and Cloud Portal',['orchName'], states=['unable to connect', 'connected', 'connecting'])
cloudPortalServices = Gauge('cloudPortalServices', 'silverpeak cloud portal service and status',['orchName','portalService','status'])

#---------#---------#---------#---------#---------#
# Appliance Metrics
#---------#---------#---------#---------#---------#

applianceAlarm = Gauge('applianceAlarm', 'summary of active alarms for given appliance',['applianceName','severity'])
applianceCPU = Gauge('applianceCPU', 'cpu utilization in porcentage for each appliance core',['applianceName','cpu_core','metric'])
applianceDiskUsage = Gauge('applianceDiskUsage', 'appliance disk utilization for each mount point',['applianceName','mount','metric'])
applianceRebootRequiered = Enum('applianceRebootRequiered', 'check with appliance if a reboot is required from changes',['applianceName'], states=['True', 'False'])
applianceMemory = Gauge('applianceMemory', 'get appliance memory related information',['applianceName','metric'])