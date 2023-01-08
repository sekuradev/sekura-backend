package main

import (
	"flag"
	"log"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"

	"github.com/sekuradev/backend/pkg/server"
)

var certFile, keyFile, caCert string

func main() {
	flag.StringVar(&certFile, "cert", "", "Server certificate file.")
	flag.StringVar(&keyFile, "key", "", "Private key file.")
	flag.Parse()

	if certFile == "" {
		log.Fatalln("flag --cert is required")
	}
	if keyFile == "" {
		log.Fatalln("flag --key is required")
	}

	creds, err := credentials.NewServerTLSFromFile(certFile, keyFile)
	if err != nil {
		log.Fatalf("error creating server credentials: %v", err)
	}
	opts := []grpc.ServerOption{
		grpc.Creds(creds),
	}
	server.NewAgentServer(opts).Serve()
}
