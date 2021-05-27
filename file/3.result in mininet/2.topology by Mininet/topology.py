
#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI


class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class MininetSchoolTopology(Topo):
    def build(self, **_opts):
        # Adding 3 routers having diffrent subnets 
        rtr1 = self.addHost('rtr1', cls=LinuxRouter, ip='10.0.0.1/24')
        rtr2 = self.addHost('rtr2', cls=LinuxRouter, ip='10.1.0.1/24')
        rtr3 = self.addHost('rtr3', cls=LinuxRouter, ip='10.2.0.1/24')
        #r4 = self.addHost('r4', cls=LinuxRouter, ip='10.3.0.1/24')

        # Adding three Switches 
        sw1 = self.addSwitch('sw1')
        sw2 = self.addSwitch('sw2')
        sw3 = self.addSwitch('sw3')
        #sw4 = self.addSwitch('sw4')

        # Linking three host to swtich in the same subnet 
        self.addLink(sw1,
                     rtr1,
                     intfName2='r1-eth1',
                     params2={'ip': '10.0.0.1/24'})

        self.addLink(sw2,
                     rtr2,
                     intfName2='r2-eth1',
                     params2={'ip': '10.1.0.1/24'})
        self.addLink(sw3,
                     rtr3,
                     intfName2='r3-eth1',
                     params2={'ip': '10.2.0.1/24'})
        #self.addLink(sw4,
        #              rtr4,
        #             intfName2='r4-eth1',
        #             params2={'ip': '10.3.0.1/24'})


        # Now we connect router-to-router connection for subnets
        self.addLink(rtr1,
                     rtr2,
                     intfName1='r1-eth2',
                     intfName2='r2-eth2',
                     params1={'ip': '10.10.0.1/24'},
                     params2={'ip': '10.10.0.2/24'})

        # Now we connect router-to-router connection for subnets
        self.addLink(rtr2,
                     rtr3,
                     intfName1='r2-eth3',
                     intfName2='r3-eth2',
                     params1={'ip': '10.100.0.3/24'},
                     params2={'ip': '10.100.0.4/24'})

        # Add router-router link in a new subnet for the router-router connection
        self.addLink(rtr3,
                     rtr1,
                     intfName1='r1-eth3',
                     intfName2='r3-eth3',
                     params1={'ip': '10.10.10.5/24'},
                     params2={'ip': '10.10.10.6/24'})


        # we add hosts to the network by specifying the default route 
        hh1 = self.addHost(name='hh1',
                          ip='10.0.0.251/24',
                          defaultRoute='via 10.0.0.1')
        hh2 = self.addHost(name='hh2',
                          ip='10.1.0.252/24',
                          defaultRoute='via 10.1.0.1')
        hh3 = self.addHost(name='hh3',
                          ip='10.2.0.100/24',
                          defaultRoute='via 10.2.0.1')
        #hh4 = self.addHost(name='hh4',
        #                  ip='10.3.0.254/24',
        #                  defaultRoute='via 10.3.0.1')
    

        # Add host-switch links
        self.addLink(sw1, hh1)
        self.addLink(sw2, hh2)
        self.addLink(sw3, hh3)
        #self.addLink(hh4, sw4)



def run():
    topo = MininetSchoolTopology()
    net = Mininet(topo=topo)

    # Here in this part of the code we Add routing for reaching networks  that are not 
    # in one to one or direct connection with one another 
    info(net['rtr1'].cmd("ip route add 10.1.0.0/24 via 10.10.0.2 dev r1-eth2"))
    info(net['rtr2'].cmd("ip route add 10.0.0.0/24 via 10.10.0.1 dev r2-eth2"))
       
    info(net['rtr2'].cmd("ip route add 10.2.0.0/24 via 10.100.0.4 dev r2-eth3"))
    info(net['rtr3'].cmd("ip route add 10.1.0.0/24 via 10.100.0.3 dev r3-eth2"))    
   
    info(net['rtr1'].cmd("ip route add 10.2.0.0/24 via 10.10.10.5 dev r3-eth3"))
    info(net['rtr3'].cmd("ip route add 10.0.0.0/24 via 10.10.10.6 dev r1-eth3"))    
    
         
    #info(net['rtr1'].cmd("route add -net 10.2.0.0/24 gw 10.100.0.6"))
    ##info(net['rtr3'].cmd("route add -net 10.0.0.0/24 gw 10.100.0.5"))    
    
    #info(net['rtr3'].cmd("route add -net 10.2.0.0/24 gw 10.100.0.5"))    
    #info(net['rtr2'].cmd("route add -net 10.2.0.0/24 gw 10.100.0.6"))    

    net.start()
    net.pingAll()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
