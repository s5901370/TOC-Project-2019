# coding=UTF-8
from transitions.extensions import GraphMachine

from utils import send_text_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
        self.count = 0

    def on_exit_user(self,event):
       	id = event['sender']['id']
       	send_text_message(id,u'你好~接下來我出幾道謎題考考你囉!')
       	send_text_message(id,u'第一題:猴子身輕站樹梢，射一水果?(1)獼猴桃 (2)荔枝 (3)柑橘 (4)葡萄 ')       	
       	return True

    def on_exit_Q1(self, event):
        text = event['message']['text']
        id = event['sender']['id']
        if text == '2':
            send_text_message(id,u'恭喜你答對第一題囉!')
            self.count+=1
        else:
            send_text_message(id,u'可惜了~不對喔~')
        send_text_message(id,'第二題:南面而坐，北面而朝。象憂亦憂，象喜亦喜，射一用物?(1)鏡子(2)年畫(3)硯台(4)油燈')
        return True

    def on_exit_Q2(self, event):
        text = event['message']['text']
        id = event['sender']['id']
        if text == '1':
            send_text_message(id,u'你能答對的確不簡單')
            self.count+=1
        else:
            send_text_message(id,u'恩~運氣不好運氣不好')
        send_text_message(id,u'第三題:鑿壁偷光，射一人物?(1)司馬光(2)劉邦(3)李世民(4)諸葛亮')
        return True

    def on_exit_Q3(self, event):
        text = event['message']['text']
        id = event['sender']['id']
        if text == '4':
            send_text_message(id,u'這麼厲害的嗎')
            self.count+=1
        else:
        	send_text_message(id,u'給你個提示，這個人，很有名')
        send_text_message(id,u'第四題:禮義廉恥，射一字?(1)四(2)八(3)德(4)羅')
        return True

    def on_exit_Q4(self, event):
        text = event['message']['text']
        id = event['sender']['id']
        if text == '4':
            send_text_message(id,u'這題蠻簡單的其實')
            self.count+=1
        else:
        	send_text_message(id,u'這你看不出來?確定?')
        send_text_message(id,u'最後一題:馨香風飄去，聞韶恐無門。射一字?(1)繪(2)望(3)聲(4)無')
        return True

    def on_exit_Q5(self, event):
        text = event['message']['text']
        id = event['sender']['id']
        if text == '3':
            send_text_message(id,u'太神拉')
            self.count+=1
        else:
        	send_text_message(id,u'錯了也不能怪你')
        send_text_message(id,u'這謎題並不容易，能答對三四題實屬不易，而你答對了{}題'.format(self.count))
        self.count = 0
        return True
# class TocMachine(GraphMachine):
#     def __init__(self, **machine_configs):
#         self.machine = GraphMachine(
#             model=self,
#             **machine_configs
#         )

#     def go2(self, event):
#         if event.get("message"):
#             text = event['message']['text']
#             return text.lower() == 'go to state1'
#         return False

#     def is_going_to_state2(self, event):
#         if event.get("message"):
#             text = event['message']['text']
#             return text.lower() == 'go to state2'
#         return False

#     def on_enter_state1(self, event):
#         print("I'm entering state1")

#         sender_id = event['sender']['id']
#         responese = send_text_message(sender_id, "I'm entering state1")
#         self.go_back()

#     def on_exit_state1(self):
#         print('Leaving state1')

#     def on_enter_state2(self, event):
#         print("I'm entering state2")

#         sender_id = event['sender']['id']
#         send_text_message(sender_id, "I'm entering state2")
#         self.go_back()

#     def on_exit_state2(self):
#         print('Leaving state2')
