class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        secret_freq: {1: 2, 2: 1, 3: 1}

        if guess[i] == secret[i]:
            bull += 1
            secret_freq[guess[i]] -= 1
            if secret_freq[guess[i]] == 0:
                del secret_freq[guess[i]]
        

        '''

        secret_freq = collections.Counter(secret)
        covered = [False] * len(secret)
        bull, cow = 0, 0

        for i in range(len(secret)):
            if guess[i] == secret[i]: 
                bull += 1
                covered[i] = True
                secret_freq[guess[i]] -= 1
                if secret_freq[guess[i]] == 0:
                    del secret_freq[guess[i]]
        
        for i in range(len(secret)):
            if covered[i]:
                continue
            if guess[i] in secret_freq:
                cow += 1
                secret_freq[guess[i]] -= 1
                if secret_freq[guess[i]] == 0:
                    del secret_freq[guess[i]]

        return f'{bull}A{cow}B' 



        