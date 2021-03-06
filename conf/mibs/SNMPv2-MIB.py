#
# PySNMP MIB module SNMPv2-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/ietf/SNMPv2-MIB
# Produced by pysmi-0.0.7 at Mon May 30 13:41:13 2016
# On host ubuntu platform Linux version 3.13.0-79-generic by user szymon
# Using Python version 3.4.3 (default, Oct 14 2015, 20:28:29) 
#
( OctetString, ObjectIdentifier, Integer, ) = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
( ModuleCompliance, ObjectGroup, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
( Bits, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, snmpModules, mib_2, Gauge32, ObjectIdentity, MibIdentifier, Counter32, TimeTicks, Counter64, Integer32, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "snmpModules", "mib-2", "Gauge32", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks", "Counter64", "Integer32", "Unsigned32")
( DisplayString, TimeStamp, TestAndIncr, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TestAndIncr", "TextualConvention")
snmpMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 1)).setRevisions(("2002-10-16 00:00", "1995-11-09 00:00", "1993-04-01 00:00",))
snmpMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1))
system = MibIdentifier((1, 3, 6, 1, 2, 1, 1))
sysDescr = MibScalar((1, 3, 6, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readonly")
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
sysUpTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
sysContact = MibScalar((1, 3, 6, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readwrite")
sysName = MibScalar((1, 3, 6, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readwrite")
sysLocation = MibScalar((1, 3, 6, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readwrite")
sysServices = MibScalar((1, 3, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,127))).setMaxAccess("readonly")
sysORLastChange = MibScalar((1, 3, 6, 1, 2, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
sysORTable = MibTable((1, 3, 6, 1, 2, 1, 1, 9), )
sysOREntry = MibTableRow((1, 3, 6, 1, 2, 1, 1, 9, 1), ).setIndexNames((0, "SNMPv2-MIB", "sysORIndex"))
sysORIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
sysORID = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
sysORDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
sysORUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 4), TimeStamp()).setMaxAccess("readonly")
snmp = MibIdentifier((1, 3, 6, 1, 2, 1, 11))
snmpInPkts = MibScalar((1, 3, 6, 1, 2, 1, 11, 1), Counter32()).setMaxAccess("readonly")
snmpInBadVersions = MibScalar((1, 3, 6, 1, 2, 1, 11, 3), Counter32()).setMaxAccess("readonly")
snmpInBadCommunityNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 4), Counter32()).setMaxAccess("readonly")
snmpInBadCommunityUses = MibScalar((1, 3, 6, 1, 2, 1, 11, 5), Counter32()).setMaxAccess("readonly")
snmpInASNParseErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 6), Counter32()).setMaxAccess("readonly")
snmpEnableAuthenTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2),))).setMaxAccess("readwrite")
snmpSilentDrops = MibScalar((1, 3, 6, 1, 2, 1, 11, 31), Counter32()).setMaxAccess("readonly")
snmpProxyDrops = MibScalar((1, 3, 6, 1, 2, 1, 11, 32), Counter32()).setMaxAccess("readonly")
snmpTrap = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 4))
snmpTrapOID = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 4, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
snmpTrapEnterprise = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 4, 3), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
snmpTraps = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 5))
coldStart = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 1)).setObjects(*())
warmStart = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 2)).setObjects(*())
authenticationFailure = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 5)).setObjects(*())
snmpSet = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 6))
snmpSetSerialNo = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 6, 1), TestAndIncr()).setMaxAccess("readwrite")
snmpMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2))
snmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2, 1))
snmpMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2, 2))
snmpBasicCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 1, 2, 1, 2)).setObjects(*(("SNMPv2-MIB", "snmpGroup"), ("SNMPv2-MIB", "snmpSetGroup"), ("SNMPv2-MIB", "systemGroup"), ("SNMPv2-MIB", "snmpBasicNotificationsGroup"), ("SNMPv2-MIB", "snmpCommunityGroup"),))
snmpBasicComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 6, 3, 1, 2, 1, 3)).setObjects(*(("SNMPv2-MIB", "snmpGroup"), ("SNMPv2-MIB", "snmpSetGroup"), ("SNMPv2-MIB", "systemGroup"), ("SNMPv2-MIB", "snmpBasicNotificationsGroup"), ("SNMPv2-MIB", "snmpCommunityGroup"), ("SNMPv2-MIB", "snmpWarmStartNotificationGroup"),))
snmpGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 8)).setObjects(*(("SNMPv2-MIB", "snmpInPkts"), ("SNMPv2-MIB", "snmpInBadVersions"), ("SNMPv2-MIB", "snmpInASNParseErrs"), ("SNMPv2-MIB", "snmpSilentDrops"), ("SNMPv2-MIB", "snmpProxyDrops"), ("SNMPv2-MIB", "snmpEnableAuthenTraps"),))
snmpCommunityGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 9)).setObjects(*(("SNMPv2-MIB", "snmpInBadCommunityNames"), ("SNMPv2-MIB", "snmpInBadCommunityUses"),))
snmpSetGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 5)).setObjects(*(("SNMPv2-MIB", "snmpSetSerialNo"),))
systemGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 6)).setObjects(*(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysObjectID"), ("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysServices"), ("SNMPv2-MIB", "sysORLastChange"), ("SNMPv2-MIB", "sysORID"), ("SNMPv2-MIB", "sysORUpTime"), ("SNMPv2-MIB", "sysORDescr"),))
snmpBasicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 7)).setObjects(*(("SNMPv2-MIB", "coldStart"), ("SNMPv2-MIB", "authenticationFailure"),))
snmpWarmStartNotificationGroup = NotificationGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 11)).setObjects(*(("SNMPv2-MIB", "warmStart"),))
snmpNotificationGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 12)).setObjects(*(("SNMPv2-MIB", "snmpTrapOID"), ("SNMPv2-MIB", "snmpTrapEnterprise"),))
snmpOutPkts = MibScalar((1, 3, 6, 1, 2, 1, 11, 2), Counter32()).setMaxAccess("readonly")
snmpInTooBigs = MibScalar((1, 3, 6, 1, 2, 1, 11, 8), Counter32()).setMaxAccess("readonly")
snmpInNoSuchNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 9), Counter32()).setMaxAccess("readonly")
snmpInBadValues = MibScalar((1, 3, 6, 1, 2, 1, 11, 10), Counter32()).setMaxAccess("readonly")
snmpInReadOnlys = MibScalar((1, 3, 6, 1, 2, 1, 11, 11), Counter32()).setMaxAccess("readonly")
snmpInGenErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 12), Counter32()).setMaxAccess("readonly")
snmpInTotalReqVars = MibScalar((1, 3, 6, 1, 2, 1, 11, 13), Counter32()).setMaxAccess("readonly")
snmpInTotalSetVars = MibScalar((1, 3, 6, 1, 2, 1, 11, 14), Counter32()).setMaxAccess("readonly")
snmpInGetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 15), Counter32()).setMaxAccess("readonly")
snmpInGetNexts = MibScalar((1, 3, 6, 1, 2, 1, 11, 16), Counter32()).setMaxAccess("readonly")
snmpInSetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 17), Counter32()).setMaxAccess("readonly")
snmpInGetResponses = MibScalar((1, 3, 6, 1, 2, 1, 11, 18), Counter32()).setMaxAccess("readonly")
snmpInTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 19), Counter32()).setMaxAccess("readonly")
snmpOutTooBigs = MibScalar((1, 3, 6, 1, 2, 1, 11, 20), Counter32()).setMaxAccess("readonly")
snmpOutNoSuchNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 21), Counter32()).setMaxAccess("readonly")
snmpOutBadValues = MibScalar((1, 3, 6, 1, 2, 1, 11, 22), Counter32()).setMaxAccess("readonly")
snmpOutGenErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 24), Counter32()).setMaxAccess("readonly")
snmpOutGetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 25), Counter32()).setMaxAccess("readonly")
snmpOutGetNexts = MibScalar((1, 3, 6, 1, 2, 1, 11, 26), Counter32()).setMaxAccess("readonly")
snmpOutSetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 27), Counter32()).setMaxAccess("readonly")
snmpOutGetResponses = MibScalar((1, 3, 6, 1, 2, 1, 11, 28), Counter32()).setMaxAccess("readonly")
snmpOutTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 29), Counter32()).setMaxAccess("readonly")
snmpObsoleteGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 10)).setObjects(*(("SNMPv2-MIB", "snmpOutPkts"), ("SNMPv2-MIB", "snmpInTooBigs"), ("SNMPv2-MIB", "snmpInNoSuchNames"), ("SNMPv2-MIB", "snmpInBadValues"), ("SNMPv2-MIB", "snmpInReadOnlys"), ("SNMPv2-MIB", "snmpInGenErrs"), ("SNMPv2-MIB", "snmpInTotalReqVars"), ("SNMPv2-MIB", "snmpInTotalSetVars"), ("SNMPv2-MIB", "snmpInGetRequests"), ("SNMPv2-MIB", "snmpInGetNexts"), ("SNMPv2-MIB", "snmpInSetRequests"), ("SNMPv2-MIB", "snmpInGetResponses"), ("SNMPv2-MIB", "snmpInTraps"), ("SNMPv2-MIB", "snmpOutTooBigs"), ("SNMPv2-MIB", "snmpOutNoSuchNames"), ("SNMPv2-MIB", "snmpOutBadValues"), ("SNMPv2-MIB", "snmpOutGenErrs"), ("SNMPv2-MIB", "snmpOutGetRequests"), ("SNMPv2-MIB", "snmpOutGetNexts"), ("SNMPv2-MIB", "snmpOutSetRequests"), ("SNMPv2-MIB", "snmpOutGetResponses"), ("SNMPv2-MIB", "snmpOutTraps"),))
mibBuilder.exportSymbols("SNMPv2-MIB", snmpInTraps=snmpInTraps, sysORTable=sysORTable, snmpOutGetNexts=snmpOutGetNexts, sysLocation=sysLocation, snmpEnableAuthenTraps=snmpEnableAuthenTraps, snmpInNoSuchNames=snmpInNoSuchNames, sysORUpTime=sysORUpTime, snmpTrap=snmpTrap, sysContact=sysContact, sysServices=sysServices, warmStart=warmStart, snmpInBadValues=snmpInBadValues, snmpObsoleteGroup=snmpObsoleteGroup, sysObjectID=sysObjectID, snmpBasicComplianceRev2=snmpBasicComplianceRev2, snmpMIBObjects=snmpMIBObjects, snmpMIB=snmpMIB, sysDescr=sysDescr, snmpInSetRequests=snmpInSetRequests, snmpInBadCommunityUses=snmpInBadCommunityUses, snmpOutGetRequests=snmpOutGetRequests, snmpTraps=snmpTraps, snmpInReadOnlys=snmpInReadOnlys, snmpMIBGroups=snmpMIBGroups, snmpInTooBigs=snmpInTooBigs, snmpSet=snmpSet, snmpOutPkts=snmpOutPkts, snmpOutTooBigs=snmpOutTooBigs, snmpInPkts=snmpInPkts, snmpTrapEnterprise=snmpTrapEnterprise, snmpInGenErrs=snmpInGenErrs, snmpOutSetRequests=snmpOutSetRequests, snmpCommunityGroup=snmpCommunityGroup, snmp=snmp, PYSNMP_MODULE_ID=snmpMIB, snmpProxyDrops=snmpProxyDrops, coldStart=coldStart, authenticationFailure=authenticationFailure, snmpInTotalReqVars=snmpInTotalReqVars, sysOREntry=sysOREntry, snmpInGetNexts=snmpInGetNexts, snmpTrapOID=snmpTrapOID, snmpOutGetResponses=snmpOutGetResponses, snmpInBadCommunityNames=snmpInBadCommunityNames, snmpSetSerialNo=snmpSetSerialNo, sysORDescr=sysORDescr, snmpInBadVersions=snmpInBadVersions, snmpMIBConformance=snmpMIBConformance, snmpGroup=snmpGroup, snmpInGetResponses=snmpInGetResponses, snmpOutBadValues=snmpOutBadValues, sysName=sysName, snmpOutGenErrs=snmpOutGenErrs, snmpOutNoSuchNames=snmpOutNoSuchNames, systemGroup=systemGroup, snmpInGetRequests=snmpInGetRequests, snmpOutTraps=snmpOutTraps, sysORID=sysORID, snmpBasicCompliance=snmpBasicCompliance, snmpBasicNotificationsGroup=snmpBasicNotificationsGroup, snmpInTotalSetVars=snmpInTotalSetVars, sysUpTime=sysUpTime, snmpSilentDrops=snmpSilentDrops, snmpInASNParseErrs=snmpInASNParseErrs, system=system, sysORLastChange=sysORLastChange, snmpMIBCompliances=snmpMIBCompliances, snmpSetGroup=snmpSetGroup, sysORIndex=sysORIndex, snmpNotificationGroup=snmpNotificationGroup, snmpWarmStartNotificationGroup=snmpWarmStartNotificationGroup)
