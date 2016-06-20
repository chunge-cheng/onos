#!/usr/bin/env python

"""
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class GeantMplsTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self )

        # add nodes, switches first...
        ATH = self.addSwitch( 's1' )
        LIS = self.addSwitch( 's2', protocols='OpenFlow13' )
        LON = self.addSwitch( 's3' )
        BRU = self.addSwitch( 's4' )
        PAR = self.addSwitch( 's5' )
        DUB = self.addSwitch( 's6' )
        MAD = self.addSwitch( 's7' )
        GEN = self.addSwitch( 's8' )
        MIL = self.addSwitch( 's9', protocols='OpenFlow13' )
        SOF = self.addSwitch( 's10' )
        BUC = self.addSwitch( 's11' )
        VIE = self.addSwitch( 's12' )
        FRA = self.addSwitch( 's13' )
        COP = self.addSwitch( 's14' )
        TLN = self.addSwitch( 's15' )
        RIG = self.addSwitch( 's16' )
        KAU = self.addSwitch( 's17' )
        POZ = self.addSwitch( 's18' )
        PRA = self.addSwitch( 's19' )
        BRA = self.addSwitch( 's20' )
        ZAG = self.addSwitch( 's21' )
        LJU = self.addSwitch( 's22', protocols='OpenFlow13' )
        BUD = self.addSwitch( 's23' )
        MLT = self.addSwitch( 's24' )
        LUX = self.addSwitch( 's25' )
        MAR = self.addSwitch( 's26' )
        HAM = self.addSwitch( 's27' )
        AMS = self.addSwitch( 's28' )


    # ... and now hosts
        ATH_host = self.addHost( 'h1' )
        LIS_host = self.addHost( 'h2' )
        LON_host = self.addHost( 'h3' )
        BRU_host = self.addHost( 'h4' )
        PAR_host = self.addHost( 'h5' )
        DUB_host = self.addHost( 'h6' )
        MAD_host = self.addHost( 'h7' )
        GEN_host = self.addHost( 'h8' )
        MIL_host = self.addHost( 'h9' )
        SOF_host = self.addHost( 'h10' )
        BUC_host = self.addHost( 'h11' )
        VIE_host = self.addHost( 'h12' )
        FRA_host = self.addHost( 'h13' )
        COP_host = self.addHost( 'h14' )
        TLN_host = self.addHost( 'h15' )
        RIG_host = self.addHost( 'h16' )
        KAU_host = self.addHost( 'h17' )
        POZ_host = self.addHost( 'h18' )
        PRA_host = self.addHost( 'h19' )
        BRA_host = self.addHost( 'h20' )
        ZAG_host = self.addHost( 'h21' )
        LJU_host = self.addHost( 'h22' )
        BUD_host = self.addHost( 'h23' )
        MLT_host = self.addHost( 'h24' )
        LUX_host = self.addHost( 'h25' )
        MAR_host = self.addHost( 'h26' )
        HAM_host = self.addHost( 'h27' )
        AMS_host = self.addHost( 'h28' )

        # add edges between switch and corresponding host
        self.addLink( ATH , ATH_host )
        self.addLink( LIS , LIS_host )
        self.addLink( LON , LON_host )
        self.addLink( BRU , BRU_host )
        self.addLink( PAR , PAR_host )
        self.addLink( DUB , DUB_host )
        self.addLink( MAD , MAD_host )
        self.addLink( GEN , GEN_host )
        self.addLink( MIL , MIL_host )
        self.addLink( SOF , SOF_host )
        self.addLink( BUC , BUC_host )
        self.addLink( VIE , VIE_host )
        self.addLink( FRA , FRA_host )
        self.addLink( COP , COP_host )
        self.addLink( TLN , TLN_host )
        self.addLink( RIG , RIG_host )
        self.addLink( KAU , KAU_host )
        self.addLink( POZ , POZ_host )
        self.addLink( PRA , PRA_host )
        self.addLink( BRA , BRA_host )
        self.addLink( ZAG , ZAG_host )
        self.addLink( LJU , LJU_host )
        self.addLink( BUD , BUD_host )
        self.addLink( MLT , MLT_host )
        self.addLink( LUX , LUX_host )
        self.addLink( MAR , MAR_host )
        self.addLink( HAM , HAM_host )
        self.addLink( AMS , AMS_host )

        # add edges between switches
        self.addLink( ATH , MIL, bw=10 )
        self.addLink( MIL , VIE, bw=10 )
        self.addLink( MIL , MAR, bw=10 )
        self.addLink( MIL , GEN, bw=10 )
        self.addLink( MIL , MLT, bw=10 )
        self.addLink( GEN , FRA, bw=10 )
        self.addLink( GEN , PAR, bw=10 )
        self.addLink( GEN , MAR, bw=10 )
        self.addLink( MAR , MAD, bw=10 )
        self.addLink( MAD , PAR, bw=10 )
        self.addLink( MAD , LIS, bw=10 )
        self.addLink( LIS , LON, bw=10 )
        self.addLink( LON , PAR, bw=10 )
        self.addLink( LON , DUB, bw=10 )
        self.addLink( LON , BRU, bw=10 )
        self.addLink( BRU , AMS, bw=10 )
        self.addLink( AMS , LUX, bw=10 )
        self.addLink( LUX , FRA, bw=10 )
        self.addLink( AMS , HAM, bw=10 )
        self.addLink( HAM , FRA, bw=10 )
        self.addLink( HAM , COP, bw=10 )
        self.addLink( COP , AMS, bw=10 )
        self.addLink( FRA , POZ, bw=10 )
        self.addLink( FRA , PRA, bw=10 )
        self.addLink( FRA , BUD, bw=10 )
        self.addLink( FRA , VIE, bw=10 )
        self.addLink( POZ , PRA, bw=10 )
        self.addLink( POZ , KAU, bw=10 )
        self.addLink( KAU , RIG, bw=10 )
        self.addLink( ZAG , VIE, bw=10 )
        self.addLink( ZAG , BUD, bw=10 )
        self.addLink( BUD , PRA, bw=10 )
        self.addLink( BUD , BRA, bw=10 )
        self.addLink( BUD , BUC, bw=10 )
        self.addLink( BUD , SOF, bw=10 )
        self.addLink( BUD , LJU, bw=10 )
        self.addLink( BUC , SOF, bw=10 )
        self.addLink( BUC , VIE, bw=10 )
        self.addLink( VIE , BRA, bw=10 )
        self.addLink( RIG , TLN, bw=10 )
        self.addLink( TLN , HAM, bw=10 )


topos = { 'att': ( lambda: GeantMplsTopo() ) }

if __name__ == '__main__':
    from onosnet import run
    run( GeantMplsTopo() )
