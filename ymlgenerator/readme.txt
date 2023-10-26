sample input file.

uhn9robin20bwk001                             #hostname 
0.6.2.8                                       #RCP version
fd02:298c:8dfe:347:b6a9:fcff:fef9:f4d4        #BMC IP
fd03:298c:8dfe:826:a90:1:1:0                  #host IP
GC sku2                                       #server kind
5.3.13.125                                    #robin version
127                                           #bond vlan
RDC                                           #RDC Type

################################################################
rcp_dc_type: ????  last parameter is present in inventry fie with rcp_dc_type


how to use this script:
         
          cd /mnt/data0/clrtsdata/robin-cluster/host-files/ymlgenerator

          1) update host details in input.txt file
                  vi input.txt

          2) sequance of host parameter should be same as per above format
         
           3) run ymlgenerate.sh  script

          4)in below path you will find directory with hostname.
             cd  /mnt/data0/clrtsdata/robin-cluster/host-files/ymlfiles
             cd <hostname>
         
          5)in that you will get invernety and os file.
         
          6) verify your files and start installation.

 
