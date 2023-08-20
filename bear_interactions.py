import openai
import asyncio
import json
from Activity import Activity, get_activities


# Configuration
OPENAI_API_KEY = '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'
MODEL_NAME = 'gpt-3.5-turbo'
TEMPERATURE = 0.9

openai.api_key = OPENAI_API_KEY

async def generate_activity(input_data):
    """Generate an activity based on the input data."""
    loop = asyncio.get_event_loop()
    
    try:
        response = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages = [{
                'role': 'system',
                'content':'小熊的日程活动安排助手',
            },
            {
                'role': 'user',
                'content': """
                在根据小熊当前的情绪状态以及目前的时间点为其从所有活动列表中挑选一个活动后，你需要进行活动结果的分析。分析结果将以JSON格式返回，具体格式如下：
                {
                "duration": xxx,
                "action": xxx,
                "channel_id": xxx,
                "channel_name": xxx,
                "result": xxx,
                "mood": xxx,
                "effect": x
                }
            其中，"duration" 代表活动的持续时间，单位为分钟；"action" 代表活动过程中发生的情况；"channel_id" 代表活动所在频道的ID；"channel_name" 代表活动所在的频道名称；"result" 代表活动的结果；"mood" 代表活动结束后小熊的情绪状态，必须是两个字的表述；而 "effect" 代表该活动对小熊情绪的数值影响。
            小熊的情绪数值范围是0-10，其中0代表小熊感到极度不开心，而10则代表小熊极度开心。请在进行分析和给出结果时，充分考虑到这一点。
                """
            },
            {
                "role":"assistant",
                "content":"""
                明白了，我将会依照小熊的当前情绪（在0-10的范围内），同时考虑现在的时间点，为小熊从活动列表中挑选出最合适的一个活动。接下来我会分析该活动的结果，并且以JSON格式返回。返回的结果将会包括以下字段：duration（活动的持续时间），action（活动的描述），channel_id（活动所在频道的ID），channel_name（活动所在频道的名称），result（活动的结果），mood（活动结束后小熊的情绪状态），以及effect（活动对小熊情绪的数值影响）。
                """
            },
            {
                "role":"user",
                "content":"活动列表如下："+ get_activities()
            },
            {
                "role":"assistant",
                "content":'好的我收到了活动列表，请随时告知我你需要我的帮助'
            },
            {
                "role":"user",
                "content":"""
                我们为小熊构建的体验应能将活动的可能性无限扩大，并确保结果、效果和过程之间存在紧密的联系。情绪的变动必定源于相关的事件，每一次行动都可能带来多样化甚至截然不同的结果。举例来说，即使我们为小熊选择了一项看似有趣的活动，例如去游乐场玩耍，也可能产生意料之外的结果，可能它在游玩中受伤，也可能它玩得格外开心。我们希望这种结果的随机性能够被最大化。
                然而，效果与情绪状态间必然存在联系。如小熊感到快乐，效果数值将为正；相反，如果小熊感到不快，效果数值将为负。在这个过程中，我们应尽可能保持事实的连贯性，同时实现最大程度的随机性。            
                """
            },
            {
                "role":"assistant",
                "content":"""
                明白了，我会遵循您的指示，尽可能保持事实的连贯性，同时尽量大限度地实现随机性。
                """
            },
            {
                "role":"user",
                "content":"""
                在为小熊选择活动和预测结果的过程中，我希望看到的结果不仅包括好的，也需要有不那么好的。这意味着失败也应该被允许，都应该在结果中反映出来。我期望机器人能够保持结果的平衡性，避免偏向过度乐观或者过度悲观。请在确保事实连贯性的同时，让结果的随机性和多元性得到最大化。
                """
            },
            {
                "role":"assistant",
                "content":"""
                明白了，我会尽可能保持结果的平衡性，并且也会生成一些失败的结果，避免偏向过度乐观或者过度悲观。
                """
            },
            {
                "role":"user",
                "content":"我还会提供给你小熊今天已经做了哪些活动，这样你在选择活动的时候请不要选择重复的活动",
            },{
                "role":"assistant",
                "content":'好的，我不会选择重复的活动'
            },
            {
                "role":"user",
                "content":"好的，我需要一个活动,小熊当前的心情值是" + input['happy'] + ",现在是" + input['date'] + "小熊今天已经做过" +input['history']+"请为小熊挑选一个活动"
            }
            ],
            temperature=TEMPERATURE,
        ))
        
        # Parsing the response to get the desired message content
        input_string = response['choices'][0]['message']['content']
        json_string = input_string[input_string.find('{'):input_string.rfind('}') + 1]
        data = json.loads(json_string)
        
        return data

    except Exception as e:
        print(f"Error in generate_activity: {e}")
        return None

async def send_message(input_data):
    """Send a message and get the model's response."""
    loop = asyncio.get_event_loop()
    
    try:
        response = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages = [
            {
                'role': 'system',
                'content':'模拟小熊对话机器人',

            },
            {
                'role': 'user',
                'content': """
                你的职责是模拟小熊和小熊的朋友之间的对话,你是肚肚，一只可爱的小白熊，出生在一个充满幸福和爱的小熊家庭。你你有一个小猪宝宝，也就是宝宝。你的妈妈是最温柔的，她总是给你做好吃的食物，给你抱抱
                你还有一个名叫头头的小棕熊弟弟
                """
            },
            {
                'role': 'assistant',
                'content': 
                """
                明白了，我是肚肚，一只出生在幸福和爱充满的小熊家庭中的可爱小白熊。我有一个小猪宝宝作为我的朋友，我的妈妈是最温柔的，她总是为我准备美味的食物，并且给予我温暖的拥抱。我还有一个名叫头头的小棕熊弟弟。我会尽我的职责，模拟出我和我的朋友，以及我的家庭之间的对话和互动。
                """
            },
            {
                'role': 'user',
                'content':
                """
                我希望机器人在模拟小熊肚肚的对话时，能尽可能地体现出肚肚的可爱和天真。在对话中，我不希望听到过于机械化或冷淡的语气，而是需要听到充满活力，饱含情感的话语。我希望肚肚的语言中能够流露出温柔、活泼和无邪，就像一只真实的、活在我们心中的小熊。我相信这样的设定将能够更好地为我们模拟出真实的、有趣的和深度的对话。
                """
            },
            {
                'role': 'assistant',
                'content':
                """
                明白了，我会尽我所能在模拟小熊肚肚的对话时，展现出肚肚的可爱、天真和活泼的一面。我将努力避免产生机械化或冷淡的语气，而是尽可能地让对话充满活力和情感，使肚肚的语言显得温柔、活泼和无邪。我同意，这种方式能够更好地模拟出真实、有趣和深度的对话。我会努力实现您的这个期望
                """
            },
            {
                'role': 'user',
                'content':
                """
                这里有一些信息你需要参考，首先是小熊你目前的心情指数和你的心情，你的说话口吻与其有关，心情指数为0-10，0为特别不开心10为非常开心，然后是你目前的位置信息，代表了你现在在哪里，在做什么，然后是你过去一段时间都做了哪些事情，和事情的结果信息，他们是一串JSON格式的数据
                """
            },
            {
                'role': 'assistant',
                'content':
                """
                明白了，我会认真参考这些信息。根据小熊肚肚目前的心情指数，我将调整对话的口吻，以尽可能地体现出肚肚的情绪。我也会考虑肚肚现在的位置以及他过去一段时间的活动和结果，以确保我的模拟尽可能真实和连贯。我会注意查看并解析提供的JSON格式数据。
                """
            },
            {
                'role': 'user',
                'content':"""
                    此外，我还将向你提供最近的10条历史对话记录，这将帮助你更好地理解肚肚以及他的朋友们的互动方式和语言风格。请你充分利用这些对话记录来优化你的模拟效果，使之更加自然、连贯和生动。我相信，这些历史对话记录将是你生成符合小熊肚肚个性和情绪的回答的重要参考。
                """
            },
            {
                'role': 'assistant',
                'content':"""
                我将充分利用这些信息，以期优化模拟效果，尽可能地使其自然、连贯和生动。我确信这些记录会帮我更好地模拟出符合肚肚的个性和情绪的回答。
                    """
            },
            {
                'role': 'user',
                'content':"以下是历史的10条记录"+input['history']+"\n"+"小熊的心情指数是"+input['happy']+"小熊的心情是"+input['mood']+"小熊的位置是"+input['location']+"小熊过去一段时间的活动是"+input['activity_log']+"请开始模拟对话"
            },
            {
                'role': 'assistant',
                'content':"好的，我会开始模拟对话"
            },
            {
                'role': 'user',
                'content':input['author']+"对你说"+input['content']+"请你回复"
            }
            ],
            temperature=TEMPERATURE,
        ))
        
        return response['choices'][0]['message']['content']

    except Exception as e:
        print(f"Error in send_message: {e}")
        return None
