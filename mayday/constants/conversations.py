__author__ = 'paytonc'

AND_THEN = '之後?'
NONE_RECORD = '''目前未有紀錄'''
TYPE_IN_CORRECT = 'Bingo! 全中'
TYPE_IN_ERROR = '輸入錯誤，請重新輸入'
TYPE_IN_WARNING = '瑪莎說：這樣不行哦\n{error_message}'
TICKET = '''
Telegram Username: @{username}
門票狀態: {status_id}
門票類型: {category_id}
日期: {date}
票面價格: {price_id}
數量: {quantity}
座位區域: {section}
座位行數: {row}
備註: {remarks}
最後更新時間: {update_at}

== 換票部分 ==
希望交換的日期: {wish_date}
希望交換的價格種類: {wish_price_id}
希望交換的數量: {wish_quantity}
'''

################
## MAIN PANEL ##
################

MAIN_PANEL_ADMIN_PANEL = '開啟Admin模式'

MAIN_PANEL_START = '''
Hello @{username} 有咩可以幫到你?
若然中途不知所措/迷失方向，請使用 /home 回到主目錄
'''

MAIN_PANEL_DONE = '''
五月之約 迪士尼門口見~!
之後你 /start 就可以再次召喚我'''

MAIN_PANEL_USERNAME_MISSING = '''
你未填Username喔...
入Setting選擇Username就可以填
否則對方就冇辦法搵到你
填寫完Username再點 /start 開始喇
'''

MAIN_PANEL_REMINDER = '''
除各認可單位收取的手續費(建議賣家提供收據或其他證明)外，只接受原價放售。
如發現黃牛，請盡公民義務舉報警方，及將證據Send到 @hk_mayday 舉報下架。
請各五迷小心交易，本telegram只提供平台(非官方)配對買賣雙方，買賣方的爭議或任何人士如遭受損失，本平台及開發者概不負責。'''

MAIN_PANEL_YELLOWCOW = '''根據記錄，你被舉報為黃牛。本平台不能再為你提供服務。bye～'''

MAIN_PANEL_TIMEOUT = '''
請按順序 
/done 
/start
重新開始
'''


#################
## POST TICKET ##
#################

POST_TICKET_ERROR = '系統錯誤 請稍後再試'
POST_TICKET_CHECK = '''請再一次確認你的門票

Telegram Username: @{username}
門票類型: {category_id}
門票狀態: {status_id}
日期: {date}
票面價格: {price_id}
數量: {quantity}
座位區域: {section}
座位行數: {row}
備註: {remarks}

== 換票部分 ==
希望交換的日期: {wish_date}
希望交換的價格種類: {wish_price_id}
希望交換的數量: {wish_quantity}
'''
POST_TICKET_INFO = '{message}係?'
POST_TICKET_INTO_DB = '你的門票已經被紀錄'
POST_TICKET_RESET = '重置完成'
POST_TICKET_START = '''如果你想放張票上來，請填寫一下內容。
(⚠️為必填項)
Telegram Username: @{username}
門票狀態: {status_id}
⚠️門票類型: {category_id}
⚠️日期: {date}
⚠️票面價格: {price_id}
⚠️數量: {quantity}
座位區域: {section}
座位行數: {row}
備註: {remarks}

== 僅限換票填寫(供配對使用) ==
若為欄位不填寫 則表示可交換任意條件
希望交換的日期: {wish_date}
希望交換的價格種類: {wish_price_id}
希望交換的數量: {wish_quantity}
'''
POST_TICKET_SECTION = '''請先填寫票面價格再輸入座位區域'''

############
## SEARCH ##
############

SEARCH_AND_THEN = '之後?'
SEARCH_CONDITION = '話畀我知你想要咩門票,介紹返'
SEARCH_CHECK = '''請再一次確認你查詢的條件.
(⚠️為必填項)
⚠️門票類別: {category_id}
門票狀態: {status_id}
日期: {date}
票面價格: {price_id}
數量: {quantity}
'''
SEARCH_TICKET_ERROR = '系統錯誤 請稍後再試'
SEARCH_TICKET_INFO = '{message}係?'
SEARCH_WITH_RESULTS = '我地搵到以下門票：\n'
SEARCH_WITHOUT_TICKETS = '暫時冇喔～不如改一改你要搵嘅條件?'
SEARCH_TOO_MUCH_TICKETS = '搵到的門票太多，請縮小範圍搜索'
SEARCH_TICKET_START = '''查詢的條件:
(⚠️為必填項)
⚠️門票類別: {category_id}
門票狀態: {status_id}
日期: {date}
票面價格: {price_id}
數量: {quantity}
'''

##################
## QUICK_SEARCH ##
##################

QUICK_SEARCH_START = '''
*根據已儲存的條件去搵*
使用之前在*搵門票*去搵現有的門票

*自動匹配換飛*
使用你已經發佈的門票去比對
你手上張飛要係:
1. 有你已經發佈咗的飛(唔好搞虛假交易，Ban硬)
2. 雙方的門票狀態: *待交易*
3. 雙方的門票類型: *換飛*
4. 對方的飛同你希望配對的飛條件*完全一樣*
'''

QUICK_SEARCH_INSERT_SUCESS = '''搜索條件已被紀錄
當前搜索條件
門票類別: {category_id}
門票狀態: {status_id}
日期: {date}
票面價格: {price_id}
數量: {quantity}
'''
QUICK_SEARCH_NULL = '''冇快速搜索的紀錄
快速搜索需要在 `搜索門票` 當中添加
'''
QUICK_SEARCH_INSERT_FAIL = '系統錯誤 請稍後再試'
QUICK_SEARCH_LIST_QUERY = '''
儲存的快速搜索條件:
門票類別: {category_id}
門票狀態: {status_id}
日期: {date}
票面價格: {price_id}
數量: {quantity}
'''


#############
## SUPPORT ##
#############

SUPPORT_LIST_EVENTS = '''
目前所知的應援活動：
'''

SUPPORT_NONE_EVENTS = '目前沒有應援活動'

SUPPORT_EVENTS_523 = '''
[轉發] 523 節目
https: // www.facebook.com / 523HKLifeTour/
'''
SUPPORT_EVENT_HOME_KONG = '''
[轉發] 《五月之約》尋回專屬HOME KONG場的感動
2006年的五月，
台上只有五月天，
台下只有熱愛他們的歌迷，
還有汗水、淚水、呼喊聲
交織著無數的感動與熱情。

讓我們一起找回最初的感動，
這是專屬香港的五月。

https: // www.facebook.com / events / 401155273603140/
'''

SUPPORT_EVENT_HOME_KONG_CREDIT = '圖片來源：《五月之約》尋回專屬Home Kong場的感動 (by May)'
SUPPORT_EVENT_BACK = '''
可選擇介紹其他應援活動
/home 回主選單
/done 結束程式
'''


############
## UPDATE ##
############

UPDATE_CHECK = '''請再一次確認你的門票
門票編號: {id}
Telegram Username: @{username}
門票類型: {category_id}
門票狀態: {status_id}
日期: {date}
票面價格: {price_id}
數量: {quantity}
座位區域: {section}
座位行數: {row}
備註: {remarks}
'''
UPDATE_ERROR = '系統錯誤 請稍後再試'
UPDATE_INFO = '{message}係?'
UPDATE_INTO_DB = '你張門票已經畀紀錄'
UPDATE_RESET = '重置完成'
UPDATE_START = '''請選擇要更新的門票'''
UPDATE_YOURS = '''
門票編號: {id}
門票狀態: {status_id}
門票類型: {category_id}
日期: {date}
票面價格: {price_id}
數量: {quantity}
座位區域: {section}
座位行數: {row}
備註: {remarks}
最後更新時間: {update_at}
'''

##########
## INFO ##
##########

INFO = '''
五月天LiFE人生無限公司 
HONG KONG 無限放大版

地點：*香港迪士尼樂園幻想道露天場地*
日期：May 4,5,6,11,12 
時間：*19:15開始*
票價：HK$1180座位 / HK$880座位 / HK$680座位 / HK$680企位 / HK$480座位/ 
[點擊查看座位圖](https://scontent.ftpe7-1.fna.fbcdn.net/v/t31.0-8/29060300_1123900231085500_5867832487083384930_o.jpg?_nc_fx=ftpe7-1&_nc_eui2=v1%3AAeHchup0xs6C6r4Frl8DxkjPp3lbPcGsWnvrEucYybvDM50CjQ-RKt568ySOmUZEXt7QT1YrfQl2RSOkqOq0pEILN5op2owZnF9XdW3jetzf-Q&oh=c4b84828c669690aec199cc69cfea1e9&oe=5B33FAFC)
'''

###########
## STATS ##
###########
STATS_NONE = '''目前未有門票紀錄'''
STATS = '''
目前的門票狀況:
更新時間: {update_at}
依門票狀態統計:
{status_distribution}

只顯示待交易門票:
{ticket_distribution}

'''
STATUS_STAT = '{status_id} : {amount}'
TICKET_STAT = '*{category_id}* {date} {price_id} 的門票有 {amount} 筆紀錄'
