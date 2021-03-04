#!/usr/bin/env python
'''
Autogenerated code using arya.py
Original Object Document Input: 
{
  "fvTenant": {
    "attributes": {
      "name": "Aardvark-2"
    },
    "children": [
      {
        "fvAp": {
          "attributes": {
            "name": "Aardvark-2-AP"
          },
          "children": [
            {
              "fvAEPg": {
                "attributes": {
                  "name": "web"
                },
                "children": [
                  {
                    "fvRsProv": {
                      "attributes": {
                        "tnVzBrCPName": "web-contract"
                      }
                    }
                  },
                  {
                    "fvRsCons": {
                      "attributes": {
                        "tnVzBrCPName": "mssql-contract"
                      }
                    }
                  },
                  {
                    "fvRsBd": {
                      "attributes": {
                        "tnFvBDName": "Aardvark-2-BD"
                      }
                    }
                  },
                  {
                    "fvRsPathAtt": {
                      "attributes": {
                        "encap": "vlan-10",
                        "tDn": "topology/pod-1/paths-101/pathep-[eth1/1]"
                      }
                    }
                  },
                  {
                    "fvRsDomAtt": {
                      "attributes": {
                        "tDn": "uni/phys-allvlans"
                      }
                    }
                  }
                ]
              }
            },
            {
              "fvAEPg": {
                "attributes": {
                  "name": "db"
                },
                "children": [
                  {
                    "fvRsProv": {
                      "attributes": {
                        "tnVzBrCPName": "mssql-contract"
                      }
                    }
                  },
                  {
                    "fvRsBd": {
                      "attributes": {
                        "tnFvBDName": "Aardvark-2-BD"
                      }
                    }
                  },
                  {
                    "fvRsPathAtt": {
                      "attributes": {
                        "encap": "vlan-10",
                        "tDn": "topology/pod-1/paths-102/pathep-[eth1/1]"
                      }
                    }
                  },
                  {
                    "fvRsDomAtt": {
                      "attributes": {
                        "tDn": "uni/phys-allvlans"
                      }
                    }
                  }
                ]
              }
            }
          ]
        }
      },
      {
        "fvCtx": {
          "attributes": {
            "name": "Aardvark-2-CTX",
            "pcEnfPref": "enforced"
          },
          "children": []
        }
      },
      {
        "fvBD": {
          "attributes": {
            "name": "Aardvark-2-BD",
            "unkMacUcastAct": "proxy",
            "unkMcastAct": "flood",
            "arpFlood": "no",
            "unicastRoute": "yes",
            "multiDstPktAct": "bd-flood"
          },
          "children": [
            {
              "fvRsCtx": {
                "attributes": {
                  "tnFvCtxName": "Aardvark-2-CTX"
                }
              }
            },
            {
              "fvSubnet": {
                "attributes": {
                  "name": "Aardvark-2-Subnet",
                  "ip": "10.1.1.1/24"
                },
                "children": []
              }
            }
          ]
        }
      },
      {
        "vzBrCP": {
          "attributes": {
            "name": "mssql-contract",
            "scope": "context"
          },
          "children": [
            {
              "vzSubj": {
                "attributes": {
                  "name": "mssql-contract_Subject"
                },
                "children": [
                  {
                    "vzRsSubjFiltAtt": {
                      "attributes": {
                        "tnVzFilterName": "ms-sql_Filter"
                      }
                    }
                  }
                ]
              }
            }
          ]
        }
      },
      {
        "vzFilter": {
          "attributes": {
            "name": "ms-sql_Filter"
          },
          "children": [
            {
              "vzEntry": {
                "attributes": {
                  "name": "ms-sql",
                  "applyToFrag": "no",
                  "arpOpc": "unspecified",
                  "dFromPort": "1433",
                  "dToPort": "1433",
                  "etherT": "ip",
                  "prot": "tcp",
                  "sFromPort": "1",
                  "sToPort": "65535",
                  "tcpRules": "unspecified",
                  "stateful": "0"
                },
                "children": []
              }
            }
          ]
        }
      },
      {
        "vzBrCP": {
          "attributes": {
            "name": "web-contract",
            "scope": "context"
          },
          "children": [
            {
              "vzSubj": {
                "attributes": {
                  "name": "web-contract_Subject"
                },
                "children": [
                  {
                    "vzRsSubjFiltAtt": {
                      "attributes": {
                        "tnVzFilterName": "http_Filter"
                      }
                    }
                  },
                  {
                    "vzRsSubjFiltAtt": {
                      "attributes": {
                        "tnVzFilterName": "https_Filter"
                      }
                    }
                  }
                ]
              }
            }
          ]
        }
      },
      {
        "vzFilter": {
          "attributes": {
            "name": "http_Filter"
          },
          "children": [
            {
              "vzEntry": {
                "attributes": {
                  "name": "http",
                  "applyToFrag": "no",
                  "arpOpc": "unspecified",
                  "dFromPort": "80",
                  "dToPort": "80",
                  "etherT": "ip",
                  "prot": "tcp",
                  "sFromPort": "1",
                  "sToPort": "65535",
                  "tcpRules": "unspecified",
                  "stateful": "0"
                },
                "children": []
              }
            }
          ]
        }
      },
      {
        "vzFilter": {
          "attributes": {
            "name": "https_Filter"
          },
          "children": [
            {
              "vzEntry": {
                "attributes": {
                  "name": "https",
                  "applyToFrag": "no",
                  "arpOpc": "unspecified",
                  "dFromPort": "443",
                  "dToPort": "443",
                  "etherT": "ip",
                  "prot": "tcp",
                  "sFromPort": "1",
                  "sToPort": "65535",
                  "tcpRules": "unspecified",
                  "stateful": "0"
                },
                "children": []
              }
            }
          ]
        }
      }
    ]
  }
}

'''
#raise RuntimeError('Please review the auto generated code before ' +
                    #'executing the output. Some placeholders will ' +
                    #'need to be changed')

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
import cobra.model.vz
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://192.168.11.1', 'admin', '1234QWer')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
topMo = cobra.model.pol.Uni('')


# build the request using cobra syntax
fvTenant = cobra.model.fv.Tenant(topMo, name='Aardvark-2')
fvAp = cobra.model.fv.Ap(fvTenant, name='Aardvark-2-AP')
fvAEPg = cobra.model.fv.AEPg(fvAp, name='web')
fvRsProv = cobra.model.fv.RsProv(fvAEPg, tnVzBrCPName='web-contract')
fvRsCons = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName='mssql-contract')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName='Aardvark-2-BD')
fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, encap='vlan-10', tDn='topology/pod-1/paths-101/pathep-[eth1/2]')
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, tDn='uni/phys-allvlans')
fvAEPg2 = cobra.model.fv.AEPg(fvAp, name='db')
fvRsProv2 = cobra.model.fv.RsProv(fvAEPg2, tnVzBrCPName='mssql-contract')
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, tnFvBDName='Aardvark-2-BD')
fvRsPathAtt2 = cobra.model.fv.RsPathAtt(fvAEPg2, encap='vlan-10', tDn='topology/pod-1/paths-102/pathep-[eth1/2]')
fvRsDomAtt2 = cobra.model.fv.RsDomAtt(fvAEPg2, tDn='uni/phys-allvlans')
fvCtx = cobra.model.fv.Ctx(fvTenant, name='Aardvark-2-CTX', pcEnfPref='enforced')
fvBD = cobra.model.fv.BD(fvTenant, name='Aardvark-2-BD', unkMacUcastAct='proxy', unkMcastAct='flood', arpFlood='no', unicastRoute='yes', multiDstPktAct='bd-flood')
fvRsCtx = cobra.model.fv.RsCtx(fvBD, tnFvCtxName='Aardvark-2-CTX')
fvSubnet = cobra.model.fv.Subnet(fvBD, name='Aardvark-2-Subnet', ip='10.1.1.1/24')
vzBrCP = cobra.model.vz.BrCP(fvTenant, name='mssql-contract')
vzSubj = cobra.model.vz.Subj(vzBrCP, name='mssql-contract_Subject')
vzRsSubjFiltAtt = cobra.model.vz.RsSubjFiltAtt(vzSubj, tnVzFilterName='ms-sql_Filter')
vzFilter = cobra.model.vz.Filter(fvTenant, name='ms-sql_Filter')
vzEntry = cobra.model.vz.Entry(vzFilter, name='ms-sql', applyToFrag='no', arpOpc='unspecified', dFromPort='1433', dToPort='1433', etherT='ip', prot='tcp', sFromPort='1', sToPort='65535', tcpRules='unspecified', stateful='0')
vzBrCP2 = cobra.model.vz.BrCP(fvTenant, name='web-contract')
vzSubj2 = cobra.model.vz.Subj(vzBrCP2, name='web-contract_Subject')
vzRsSubjFiltAtt2 = cobra.model.vz.RsSubjFiltAtt(vzSubj2, tnVzFilterName='http_Filter')
vzRsSubjFiltAtt3 = cobra.model.vz.RsSubjFiltAtt(vzSubj2, tnVzFilterName='https_Filter')
vzFilter2 = cobra.model.vz.Filter(fvTenant, name='http_Filter')
vzEntry2 = cobra.model.vz.Entry(vzFilter2, name='http', applyToFrag='no', arpOpc='unspecified', dFromPort='80', dToPort='80', etherT='ip', prot='tcp', sFromPort='1', sToPort='65535', tcpRules='unspecified', stateful='0')
vzFilter3 = cobra.model.vz.Filter(fvTenant, name='https_Filter')
vzEntry3 = cobra.model.vz.Entry(vzFilter3, name='https', applyToFrag='no', arpOpc='unspecified', dFromPort='443', dToPort='443', etherT='ip', prot='tcp', sFromPort='1', sToPort='65535', tcpRules='unspecified', stateful='0')


# commit the generated code to APIC
print(toXMLStr(topMo))
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)
