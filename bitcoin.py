class Py3status:


    def bitcoin(self, json, i3status_config):
        """
        Display the latest bitcoin/dollar price from bitstamp.net
        """
        import time

        response = {'full_text':'BTC: ', 'name':'bitcoin', 'color':'#8080FF' }
        response['cached_until'] = time.time() + 5 # refresh every 5s
        position = 0

        try:
            import requests

            r = requests.get('https://www.bitstamp.net/api/ticker/')
            ticker = r.json()

            response['full_text'] += '$' + ticker['last']

        except Exception as e:
            response['color'] = '#ff0000'
        finally:
            return (position, response)
