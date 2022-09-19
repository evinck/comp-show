Simple script to show what's in a OCI compartment. 
Requires the OCI SDK for python to be installed (https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/pythonsdk.htm)

usage: comp-show.py [-h] [--profile PROFILE_NAME] compartment_id

positional arguments:
  compartment_id        the compartment id

optional arguments:
  -h, --help            show this help message and exit
  --profile PROFILE_NAME
                        the oci profile name


example ouput :

{
  "CustomerDnsZone": {
  "number": 1,
  "items": {
   "0.10.in-addr.arpa": "ocid1.dns-zone.oc1.eu-frankfurt-1.aaaaaaaa4shfg3my3tyfuzq6o4lw67bgg3xis7vp2e3sbva6pjumkf56bakq"
  }
 },
 "DnsResolver": {
  "number": 1,
  "items": {
   "vcn": "ocid1.dnsresolver.oc1.eu-frankfurt-1.amaaaaaanmvrbeaajhqph7b27ezg3q7yputp3ykx4k2hpu7tzewwcf4alj6q"
  }
 },
 "InternetGateway": {
  "number": 1,
  "items": {
   "Internet Gateway vcn": "ocid1.internetgateway.oc1.eu-frankfurt-1.aaaaaaaa6xxs3osvu4p5rem6plkhggipbicytiqdpdyotrkr6sq6njdmor2q"
  }
 },
 "DHCPOptions": {
  "number": 1,
  "items": {
   "Default DHCP Options for vcn": "ocid1.dhcpoptions.oc1.eu-frankfurt-1.aaaaaaaaybxel2cxymwmtinribs3zuocbu3m2t3fvwc3566oitcap2ouig3a"
  }
 },
 "RouteTable": {
  "number": 1,
  "items": {
   "Default Route Table for vcn": "ocid1.routetable.oc1.eu-frankfurt-1.aaaaaaaaplf4mdrgr76vdd4ubjqrbvohfltfladdxknmb3ibnvjm4uz4hf2q"
  }
 },
 "SecurityList": {
  "number": 1,
  "items": {
   "Default Security List for vcn": "ocid1.securitylist.oc1.eu-frankfurt-1.aaaaaaaaoo3hpmaykwecaxere2nvpxbd6xrn2bm4xrxl6b3anhzvxuditaaq"
  }
 },
 "Vcn": {
  "number": 1,
  "items": {
   "vcn": "ocid1.vcn.oc1.eu-frankfurt-1.amaaaaaanmvrbeaa2tjfjmwr5td3lx35gzlgzicmu6l4fjp2inyxm7ibhiga"
  }
 }
}