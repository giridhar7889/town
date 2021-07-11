import binascii
import json
from collections import OrderedDict
from uuid import uuid4

import Crypto

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, request
from rest_framework.views import APIView


class blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.nodes = set()
        # Generate random number to be used as node_id
        self.node_id = str(uuid4()).replace('-', '')
        # Create genesis block
        self.create_block(0, '00')

    def register_node(self, node_url):
        """
        Add a new node to the list of nodes
        """
        ...

    def verify_transaction_signature(self, sender_address, signature, transaction):
        """
        Check that the provided signature corresponds to transaction
        signed by the public key (sender_address)
        """
        ...

    def submit_transaction(self, sender_address, recipient_address, value, signature):
        """
        Add a transaction to transactions array if the signature verified
        """
        ...

    def create_block(self, nonce, previous_hash):
        """
        Add a block of transactions to the blockchain
        """
        ...

    def hash(self, block):
        """
        Create a SHA-256 hash of a block
        """
        ...

    def proof_of_work(self):
        """
        Proof of work algorithm
        """
        ...

    def valid_proof(self, transactions, last_hash, nonce, difficulty=MINING_DIFFICULTY):
        """
        Check if a hash value satisfies the mining conditions. This function is used within the proof_of_work function.
        """
        ...

    def valid_chain(self, chain):
        """
        check if a bockchain is valid
        """
        ...

    def resolve_conflicts(self):
        """
        Resolve conflicts between blockchain's nodes
        by replacing our chain with the longest one in the network.
        """
        ...


class Transaction:
    def __init__(self, sender_address, sender_private_key, recipient_address, value):
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.value = value

    def __getattr__(self, attr):
        return self.data[attr]

    def to_dict(self):
        return OrderedDict({'sender_address': self.sender_address,
                            'recipient_address': self.recipient_address,
                            'value': self.value})

    def sign_transaction(self):
        """
        Sign transaction with private key
        """
        private_key = RSA.importKey(binascii.unhexlify(self.sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')


def new_wallet(request):
    if request.method == 'GET':
        random_gen = Crypto.Random.new().read
        private_key = RSA.generate(1024, random_gen)
        public_key = private_key.publickey()
        response = {
            'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
            'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
        }

        return JsonResponse(response)


class generate_transaction(APIView):
    def post(self, request, *args, **kwargs):
        sender_address = request.data['sender_address']
        print(sender_address)
        sender_private_key = request.data['sender_privatekey']
        recipient_address = request.data['recipient_address']
        value = request.data['amount']

        transaction = Transaction(sender_address, sender_private_key, recipient_address, value)

        response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()}

        return Response(status=status.HTTP_201_CREATED, data=response)
