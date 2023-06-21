# Torrent
a simple Torrent clone to share and get files without any thirdparty server

Peer Server Cli command 
<ul>
<li> get [file Name] :gets a file from another online peer in the network using file Name</li>

<li>share [file Name] :Notice the tracker server that this peer has chuncks of that specific file </li>

<li>log: outputs the log of this peer server </li>

<li>q: disconnecting from the network</li>

</ul>


Tracker Server Cli command

<li> get [file Name] :gets a file from another online peer in the network using file Name</li>

<li> file_logs [file Name/all] :return all the logs related to an specific file in the network or all the files in the network </li>

<li>log: outputs the log of this peer server </li>

<li>online_users: returns current users that are online in the network</li>


</ul>


<b>Keep alive system</b>
</br>
when we are going to quit one peer we press q command and the peer send a message to the tracker server so that it notifies that the peer wants to quit


