#
# PySNMP MIB module WHISP-TCV2-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/WHISP-TCV2-MIB
# Produced by pysmi-0.0.7 at Wed Oct 12 12:15:46 2016
# On host ? platform ? version ? by user ?
# Using Python version 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)]
#
( OctetString, ObjectIdentifier, Integer, ) = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( ModuleIdentity, IpAddress, Unsigned32, iso, TimeTicks, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, MibIdentifier, ObjectIdentity, Integer32, Gauge32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Unsigned32", "iso", "TimeTicks", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "MibIdentifier", "ObjectIdentity", "Integer32", "Gauge32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
( whispModules, ) = mibBuilder.importSymbols("WHISP-GLOBAL-REG-MIB", "whispModules")
whispTextualConventionsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 3))
class WhispMACAddress(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(6,6)
    fixedLength = 6

class WhispLUID(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,4095)

class EventString(OctetString, TextualConvention):
    displayHint = '2048a'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,2048)

mibBuilder.exportSymbols("WHISP-TCV2-MIB", PYSNMP_MODULE_ID=whispTextualConventionsModule, whispTextualConventionsModule=whispTextualConventionsModule, WhispMACAddress=WhispMACAddress, EventString=EventString, WhispLUID=WhispLUID)
