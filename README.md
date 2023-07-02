#  🌐 Torrent: A Simple P2P File Sharing Project 

Welcome to Torrent! This is a simple project for sharing and acquiring files without any third-party server. This Torrent clone allows you to quickly share files in a peer-to-peer network. We also implement a `keep alive` system to manage network connections.

## 🛠️ Commands 

### Peer Server CLI Commands

- **get [file Name]** - Fetches a file from another online peer in the network using file name.
- **share [file Name]** - Notifies the tracker server that this peer has chunks of a specific file.
- **log** - Outputs the log of this peer server.
- **q** - Disconnects from the network.

### Tracker Server CLI Commands

- **get [file Name]** - Fetches a file from another online peer in the network using file name.
- **file_logs [file Name/all]** - Returns all the logs related to a specific file in the network or all the files in the network.
- **log** - Outputs the log of this peer server.
- **online_users** - Returns current users that are online in the network.

## 🔄 Keep Alive System

When a peer wants to quit, the 'q' command is used. The peer then sends a message to the tracker server to notifythat it wants to quit the network. This way, the peer can gracefully leave the network without disrupting the service.

## 🚀 Getting Started

To get started, you'll need to clone this repository to your local machine. Once that's done, you can run the tracker server and peer server separately on different command line interfaces (CLI).

Please note that both the peer and tracker servers need to be running for the network to operate.

## 👋 Contributing

We encourage you to contribute to Torrent! Please check out the [Contributing to Torrent guide](CONTRIBUTION.md) for guidelines
