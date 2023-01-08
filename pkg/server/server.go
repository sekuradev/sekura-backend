package server

import (
	"flag"
)

var (
	serverName = flag.String("serverName", "localhost", "The server name")
	port       = flag.Int("port", 50051, "The server port")
)

type Server interface {
	Serve()
}
