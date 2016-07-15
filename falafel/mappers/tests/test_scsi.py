from falafel.mappers.scsi import get_scsi
from falafel.tests import context_wrap

SCSI_OUTPUT = """
Attached devices:
Host: scsi0 Channel: 03 Id: 00 Lun: 00
  Vendor: HP       Model: P420i            Rev: 3.54
  Type:   RAID                             ANSI  SCSI revision: 05
Host: scsi0 Channel: 00 Id: 00 Lun: 00
  Vendor: HP       Model: LOGICAL VOLUME   Rev: 3.54
  Type:   Direct-Access                    ANSI  SCSI revision: 05
Host: scsi0 Channel: 00 Id: 00 Lun: 01
  Vendor: HP       Model: LOGICAL VOLUME   Rev: 3.54
  Type:   Direct-Access                    ANSI  SCSI revision: 05
Host: scsi0 Channel: 00 Id: 00 Lun: 02
  Vendor: HP       Model: LOGICAL VOLUME   Rev: 3.54
  Type:   Direct-Access                    ANSI  SCSI revision: 05
Host: scsi0 Channel: 00 Id: 00 Lun: 03
  Vendor: HP       Model: LOGICAL VOLUME   Rev: 3.54
  Type:   Direct-Access                    ANSI  SCSI revision: 05
"""

def test_scsi():
    context = context_wrap(SCSI_OUTPUT)
    result = get_scsi(context)
    assert len(result) == 5
    r = result[0]
    assert r["host"] == "scsi0"
    assert r["channel"] == "03"
    assert r["id"] == "00"
    assert r["lun"] == "00"
    assert r["vendor"] == "HP"
    assert r["model"] == "P420i"
    assert r["rev"] == "3.54"
    assert r["type"] == "RAID"
    assert r["ansi__scsi_revision"] == "05"

    r =  result[1]
    assert r["model"] == "LOGICAL VOLUME"

    r = result[4]
    assert r["type"] == "Direct-Access"
