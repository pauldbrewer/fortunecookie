#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
class MainHandler(webapp2.RequestHandler):

    def getFortune(self):
        fortunes = ["You will receive enlightenment", "You will win the Lottery", "You will find your soulmate"]
        dailyFortune = random.choice(fortunes)
        fortune = dailyFortune
        return fortune

    def getLuckyNumber(self):
        luckyNumber = random.randint(1, 100)
        num_sent = str(luckyNumber)
        num_para = num_sent
        return  num_para

    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        daily_fortune = "<p>Your Fortune: <strong>" + self.getFortune() + "</strong></p>"
        lucky_number = "<strong>" + self.getLuckyNumber() + "</strong>"

        cookie_again_button = "<p><a href='.'><button>Another cookie plz!</button></a></p>"

        content = (header + daily_fortune + "Your Lucky Number is: " + lucky_number + cookie_again_button)

        self.response.write(content)



routes = [
    ('/', MainHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
