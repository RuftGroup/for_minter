import requests
import urllib
import base64

class MinterApi:

    def __init__(self, is_test=False):
        self.is_test = is_test
        if is_test:
            self.url = 'https://api.testnet.minter.stakeholder.space'
        else:
            self.url = 'https://api.minter.stakeholder.space'

    '''
    public function getStatus(): \stdClass
    {
        return $this->get('/status');
    }
    '''

    def getStatus(self):
        return requests.get(self.url + '/status').json()


    '''
        public function getCandidate(string $publicKey, ?int $height = null): \stdClass
    {
        $params = ['pub_key' => $publicKey];

        if($height) {
            $params['height'] = $height;
        }

        return $this->get('/candidate', $params);
    }

    '''

    def getCandidate(self, public_key, height = None):
        params = {'pub_key' : public_key}
        if height is not  None:
            params['height'] = height
        return requests.get(self.url + '/candidate', params).json()

    '''
    public function getValidators(?int $height = null): \stdClass
    {
        return $this->get('/validators', ($height ? ['height' => $height] : null));
    }    
    '''

    def getValidators(self, height = None):
        return requests.get(self.url + '/validators', {'height' : height} if height is not None else None).json()

    '''
    public function getBalance(string $address, ?int $height = null): \stdClass
    {
        $params = ['address' => $address];

        if($height) {
            $params['height'] = $height;
        }

        return $this->get('/address', $params);
    }
    '''

    def getBalance(self, address, height = None):
        params = {'address' : address}
        if height is not  None:
            params['height'] = height
        return requests.get(self.url + '/address', params).json()

    '''
    public function getNonce(string $address): int
    {
        return $this->getBalance($address)->result->transaction_count + 1;
    }
    '''

    def getNonce(self, address):
        return int(self.getBalance(address)['result']['transaction_count']) + 1


    '''
    public function send(string $tx): \stdClass
    {
        return $this->get('/send_transaction', ['tx' => $tx]);
    }
    '''

    def send(self, tx):
        return requests.get(self.url + '/send_transaction', {'tx' : tx})

    '''
    public function getTransaction(string $hash): \stdClass
    {
        return $this->get('/transaction',  ['hash' => $hash]);
    }
    '''

    def getTransaction(self, hash):
        return requests.get(self.url + '/transaction', {'hash': hash})

    '''
    public function getBlock(int $height): \stdClass
    {
        return $this->get('/block', ['height' => $height]);
    }
    '''

    def getBlock(self, height):
        return requests.get(self.url + '/block', {'height': height}).json()

    '''
    public function getEvents(int $height): \stdClass
    {
        return $this->get('/events', ['height' => $height]);
    }
    '''

    def getEvents(self, height):
        return requests.get(self.url + '/events', {'height': height}).json()

    '''
    public function getCandidates(?int $height = null, ?bool $includeStakes = false): \stdClass
    {
        $params = [];

        if($includeStakes) {
            $params['include_stakes'] = 'true';
        }

        if($height) {
            $params['height'] = $height;
        }

        return $this->get('/candidates', $params);
    }
    '''

    def getCandidates(self, height=None, includeStakes=False):
        params = {}
        if height is not None:
            params['height'] = height
        if includeStakes:
            params['include_stakes'] = True
        return requests.get(self.url + '/candidates', params).json()

    '''
    public function getCoinInfo(string $symbol, ?int $height = null): \stdClass
    {
        $params = ['symbol' => $symbol];

        if($height) {
            $params['height'] = $height;
        }

        return $this->get('/coin_info', $params);
    }
    '''

    def getCoinInfo(self, symbol, height = None):
        params = {'symbol': symbol}
        if height is not None:
            params['height'] = height
        return requests.get(self.url + '/coin_info', params).json()

    '''
    public function estimateCoinSell(string $coinToSell, string $valueToSell, string $coinToBuy, ?int $height = null): \stdClass
    {
        $params = [
            'coin_to_sell' => $coinToSell,
            'value_to_sell' => $valueToSell,
            'coin_to_buy' => $coinToBuy
        ];

        if($height) {
            $params['height'] = $height;
        }

        return $this->get('/estimate_coin_sell', $params);
    }
    '''

    def estimateCoinSell(self, coinToSell, valueToSell, coinToBuy, height = None):
        params = {
            'coin_to_sell': coinToSell,
            'value_to_sell': valueToSell,
            'coin_to_buy': coinToBuy
        }
        if height is not None:
            params['height'] = height
        return requests.get(self.url + '/estimate_coin_sell', params).json()

    '''
    public function estimateCoinBuy(string $coinToSell, string $valueToBuy, string $coinToBuy, ?int $height = null): \stdClass
    {
        $params = [
            'coin_to_sell' => $coinToSell,
            'value_to_buy' => $valueToBuy,
            'coin_to_buy' => $coinToBuy
        ];

        if($height) {
            $params['height'] = $height;
        }

        return $this->get('/estimate_coin_buy', $params);
    }    
    '''

    def estimateCoinBuy(self, coinToSell, valueToBuy, coinToBuy, height = None):
        params = {
            'coin_to_sell': coinToSell,
            'value_to_buy': valueToBuy,
            'coin_to_buy': coinToBuy
        }

        if height is not None:
            params['height'] = height

        return requests.get(self.url + '/estimate_coin_buy', params).json()

    '''
    public function estimateTxCommission(string $tx): \stdClass
    {
        return $this->get('/estimate_tx_commission', ['tx' => $tx]);
    }
    '''

    def estimateTxCommission(self, tx):
        return requests.get(self.url + '/estimate_tx_commission', {'tx': tx}).json()


    '''
        public function getTransactions(string $query, ?int $page = null, ?int $perPage = null): \stdClass
    {
        $params = ['query' => $query];

        if($page) {
            $params['page'] = $page;
        }

        if($perPage) {
            $params['perPage'] = $perPage;
        }


        return $this->get('/transactions', $params);
    }
    '''

    def getTransactions(self, query, page=None, perPage = None):
        params = {'query': query}
        if page is not None:
            params['page'] = page
        if perPage is not None:
            params['perPage'] = perPage
        return requests.get(self.url + '/transactions', params).json()

    '''
    public function getUnconfirmedTxs(?int $limit = null): \stdClass
    {
        return $this->get('/unconfirmed_txs', ($limit ? ['limit' => $limit] : null));
    }
    '''


    def getUnconfirmedTxs(self, limit = None):
        return requests.get(self.url + '/unconfirmed_txs', {'limit': limit} if limit is not None else None).json()


    '''
    public function getMaxGasPrice(?int $height = null): \stdClass
    {
        return $this->get('/max_gas', ($height ? ['height' => $height] : null));
    }
    '''

    def getMaxGasPrice(self, height = None):
        return requests.get(self + '/max_gas', {'height': height} if height is not None else None).json()

    '''
    public function getMinGasPrice(): \stdClass
    {
        return $this->get('/min_gas_price');
    }
    '''

    def getMinGasPrice(self):
        return requests.get(self.url + '/min_gas_price').json()

    '''
    public function getMissedBlocks(string $pubKey, ?int $height = null): \stdClass
    {
        $params = ['pub_key' => $pubKey];
        if($height) {
            $params['height'] = $height;
        }

        return $this->get('/missed_blocks', $params);
    }
    '''

    def getMissedBlocks(self, pubKey, height = None):
        params = {'pub_key': pubKey}
        if height is not None:
            params['height'] = height;
        return requests.get(self.url + '/missed_blocks', params).json()



