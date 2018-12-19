# coding=UTF-8
from bottle import route, run, request, abort, static_file
from utils import send_text_message
from fsm import TocMachine

VERIFY_TOKEN = "a88"
machine = TocMachine(
    states=[
        'user',
        'Q1',
        'Q2',
        'Q3',
        'Q4',
        'Q5'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Q1',
            #'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'Q1',
            'dest': 'Q2'
            # 'conditions': 'go2'
        },
        {
            'trigger': 'advance',
            'source': 'Q2',
            'dest': 'Q3'
            # 'conditions': 'go3'
        },
        {
            'trigger': 'advance',
            'source': 'Q3',
            'dest': 'Q4'
            # 'conditions': 'go4'
        },
        {
            'trigger': 'advance',
            'source': 'Q4',
            'dest': 'Q5'
            # 'conditions': 'go5'
        },
        {
            'trigger': 'advance',
            'source': 'Q5',
            'dest': 'user'
            # 'conditions': 'go_back'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        #send_text_message(body['entry'][0]['messaging'][0]['sender']['id'],u'把把包')
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
