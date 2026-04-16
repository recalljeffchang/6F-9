import re

filename = "5F-29-PTO-Jap.html"

new_data = '''const reportData = {
            plans: {
                A: {
                    id: 'A',
                    type: 'indoor',
                    title: '方案 A：未來科技與極致美學',
                    subtitle: '麻布台 & 六本木',
                    desc: '多出週五半天，完美分攤行程！週五先去六本木與東京鐵塔看夜景，週六全心沉浸在麻布台與 teamLab。',
                    recommended: false,
                    chartData: [9, 9, 8, 8, 9, 8],
                    schedule: {
                        Fri: [
                            { time: '15:00', item: 'RED° 東京鐵塔', loc: 'RED° TOKYO TOWER', toilet: '東京鐵塔內設有無障礙設施', note: '日本最大電競樂園，青少年體驗 VR，長輩可登塔觀景。', img: IMG.tokyo_tower, mapUrl: 'https://maps.google.com/?q=RED+TOKYO+TOWER', transit: { icon: '🚝', method: '東京單軌 → 濱松町步行', duration: '約 35 分鐘', note: '羽田搭單軌到濱松町，步行或轉計程車至東京鐵塔' } },
                            { time: '18:00', item: '六本木晚餐 & 夜散步', loc: '六本木 Hills 周邊', toilet: '六本木 Hills 各樓層廁所充足', note: '高級餐廳群，夜景漂亮。長輩用餐後可在展望台休息。', img: IMG.roppongi, mapUrl: 'https://maps.google.com/?q=Roppongi+Hills+Tokyo', transit: { icon: '🚕', method: '計程車', duration: '約 5 分鐘', note: '東京鐵塔到六本木 Hills 建議搭計程車' } },
                            { time: '21:00', item: '🏨 返回飯店', loc: 'Hotel Villa Fontaine Grand 羽田空港', toilet: '飯店大廳有舒適休息區', note: '第一天不需太累，滿載夜景回羽田休息。', img: IMG.airport, mapUrl: 'https://maps.google.com/?q=Hotel+Villa+Fontaine+Grand+Haneda+Airport', transit: { icon: '🚕', method: '計程車', duration: '約 30 分鐘', note: '六本木搭計程車直達羽田機場飯店' } }
                        ],
                        Sat: [
                            { time: '10:00', item: 'teamLab Borderless', loc: 'Azabudai Hills', toilet: '商場廁所極為豪華', note: '需預約！沉浸式光影展，青少年拍照首選，長輩也會震撼。', img: IMG.teamlab, mapUrl: 'https://maps.google.com/?q=teamLab+Borderless+Azabudai+Hills', transit: { icon: '🚝', method: '東京單軌 → 日比谷線', duration: '約 40 分鐘', note: '轉日比谷線至神谷町站' } },
                            { time: '13:00', item: '麻布台之丘午餐', loc: 'Azabudai Hills 餐廳層', toilet: '各樓層皆有座位區', note: '東京新地標，餐廳等級高，環境極舒適。建議提前訂位。', img: IMG.azabudai, mapUrl: 'https://maps.google.com/?q=Azabudai+Hills+Tokyo', transit: { icon: '🚶', method: '步行', duration: '約 3 分鐘', note: '同棟商場內' } },
                            { time: '15:00', item: '麻布台精品與庭園漫步', loc: 'Azabudai Hills 廣場', toilet: '中央廣場', note: '沒有趕行程壓力，全家人在此度過悠閒的精緻下午。', img: IMG.azabudai, mapUrl: 'https://maps.google.com/?q=Azabudai+Hills+Tokyo', transit: { icon: '🚶', method: '步行', duration: '約 5 分鐘', note: '庭園散步' } },
                            { time: '18:00', item: '銀座晚餐 (自由選擇)', loc: 'Ginza', toilet: '各大百貨均有', note: '搭乘日比谷線直達銀座，享受頂級美食與購物。', img: IMG.night_view, mapUrl: 'https://maps.google.com/?q=Ginza+Tokyo', transit: { icon: '🚃', method: '日比谷線', duration: '約 10 分鐘', note: '神谷町搭日比谷線至銀座' } },
                            { time: '20:30', item: '🏨 返回飯店', loc: 'Hotel Villa Fontaine Grand 羽田空港', toilet: '', note: '從銀座回羽田非常方便快捷。', img: IMG.airport, mapUrl: 'https://maps.google.com/?q=Hotel+Villa+Fontaine+Grand+Haneda+Airport', transit: { icon: '🚃', method: '淺草線直通京急', duration: '約 35 分鐘', note: '東銀座站搭淺草線(往羽田)免轉車直達' } }
                        ],
                        Sun: [
                            { time: '09:00', item: '品川水族館', loc: 'Maxell Aqua Park Shinagawa', toilet: '館內設有長椅休息區', note: '品川站旁，室內聲光水母秀。離羽田僅 15 分鐘電車。', img: IMG.aquarium, mapUrl: 'https://maps.google.com/?q=Maxell+Aqua+Park+Shinagawa', transit: { icon: '🚝', method: '京急線', duration: '約 15 分鐘', note: '從羽田機場搭京急線直達品川站' } },
                            { time: '11:00', item: '品川 Wing 快速掃貨', loc: 'Wing Takanawa', toilet: '站前商場', note: '最後採買藥妝零食。', img: IMG.shopping, mapUrl: 'https://maps.google.com/?q=Wing+Takanawa+Shinagawa', transit: { icon: '🚶', method: '步行', duration: '約 3 分鐘', note: '水族館出來過馬路' } },
                            { time: '12:00', item: '🚕 前往羽田機場', loc: '品川 → 羽田', toilet: '', note: '準備報到回台。', img: IMG.airport, mapUrl: 'https://maps.google.com/?q=Haneda+Airport+International+Terminal', transit: { icon: '🚃', method: '京急線', duration: '約 15 分鐘', note: '直達航班' } }
                        ]
                    }
                },
                B: {
                    id: 'B',
                    type: 'indoor',
                    title: '方案 B：動畫根基與吉卜力迷蹤',
                    subtitle: '三鷹 & 中野',
                    desc: '週五先跑市區中野與新宿，週末全天就留給悠閒的吉卜力與吉祥寺。長輩零負擔！',
                    recommended: false,
                    chartData: [8, 9, 6, 7, 8, 4],
                    schedule: {
                        Fri: [
                            { time: '15:00', item: '中野百老匯', loc: 'Nakano Broadway', toilet: '2 樓有舒適廁所', note: '懷舊動漫聖地，二手公仔極多。長輩可逛樓下民生超市。', img: IMG.nakano, mapUrl: 'https://maps.google.com/?q=Nakano+Broadway', transit: { icon: '🚃', method: '京急轉 JR', duration: '約 50 分鐘', note: '從羽田搭京急→品川轉 JR 山手/中央線' } },
                            { time: '18:00', item: '新宿 3D 貓打卡與晚餐', loc: 'Shinjuku', toilet: '新宿站各百貨廁所', note: '打卡巨型 3D 貓，並在新宿享受燒肉或壽司大餐。', img: IMG.night_view, mapUrl: 'https://maps.google.com/?q=Cross+Shinjuku+Vision+3D+Cat', transit: { icon: '🚃', method: 'JR 中央線', duration: '約 5 分鐘', note: '中野→新宿僅一站' } },
                            { time: '21:00', item: '🏨 返回飯店', loc: 'Hotel Villa Fontaine Grand 羽田空港', toilet: '', note: '搭乘山手線轉單軌回飯店。', img: IMG.airport, mapUrl: '', transit: { icon: '🚃', method: 'JR 轉單軌', duration: '約 45 分鐘', note: '新宿搭山手線到濱松町轉東京單軌' } }
                        ],
                        Sat: [
                            { time: '10:00', item: '吉卜力美術館', loc: 'Ghibli Museum, Mitaka', toilet: '館內有咖啡廳可久坐', note: '必須預約！青少年朝聖地，長輩欣賞手工建築美學。', img: IMG.ghibli, mapUrl: 'https://maps.google.com/?q=Ghibli+Museum+Mitaka', transit: { icon: '🚃', method: 'JR 中央線 → 公車', duration: '約 50 分鐘', note: '羽田搭京急→品川轉 JR 中央到三鷹，再搭接駁車' } },
                            { time: '13:30', item: '吉祥寺午餐與井之頭公園', loc: 'Kichijoji', toilet: '公園與商場皆有廁所', note: '在地美食天堂。用完餐在井之頭公園散步。', img: IMG.food, mapUrl: '', transit: { icon: '🚶', method: '步行 / 公車', duration: '約 15 分鐘', note: '從美術館沿玉川上水步行' } },
                            { time: '15:30', item: '杉並動畫博物館', loc: 'Suginami Animation Museum', toilet: '室內小型場館', note: '免費，介紹日本動畫製作過程。', img: IMG.anime, mapUrl: '', transit: { icon: '🚃', method: 'JR 中央線', duration: '約 15 分鐘', note: '吉祥寺搭 JR 到荻窪站' } },
                            { time: '17:30', item: '吉祥寺商圈晚餐與掃貨', loc: 'Kichijoji Sun Road', toilet: '百貨店', note: '藥妝、雜貨天堂。長輩可在百貨休息。', img: IMG.street, mapUrl: '', transit: { icon: '🚃', method: 'JR 中央線', duration: '約 10 分鐘', note: '荻窪搭 JR 回吉祥寺' } },
                            { time: '20:30', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '週末時間充裕，不用趕車。', img: IMG.airport, mapUrl: '', transit: { icon: '🚃', method: 'JR 中央線 → 京急', duration: '約 60 分鐘', note: '吉祥寺到品川轉京急' } }
                        ],
                        Sun: [
                            { time: '09:30', item: '羽田機場免稅店巡禮', loc: 'Haneda Terminal 3', toilet: '', note: '睡到飽，直接在機場商場買好買滿。', img: IMG.airport, mapUrl: '', transit: { icon: '🚶', method: '直結', duration: '1 分鐘', note: '飯店走出大廳即是' } },
                            { time: '12:00', item: '🛫 準備報到歸國', loc: 'Haneda', toilet: '', note: '輕鬆結束假期。', img: IMG.airport, mapUrl: '', transit: { icon: '🚶', method: '直結', duration: '-', note: '' } }
                        ]
                    }
                },
                C: {
                    id: 'C',
                    type: 'indoor',
                    title: '方案 C：微縮世界與室內樂園',
                    subtitle: '台場 & 豐洲',
                    desc: '有了週五下午，能把看展與樂園分開，小孩玩得更盡興，老人家也免受奔波之苦。',
                    recommended: false,
                    chartData: [9, 8, 8, 8, 8, 9],
                    schedule: {
                        Fri: [
                            { time: '15:00', item: 'Small Worlds Tokyo', loc: '有明', toilet: '無障礙設施與沙發區', note: '世界最大室內微縮模型。', img: IMG.miniature, mapUrl: '', transit: { icon: '🚝', method: '臨海線 → 海鷗號', duration: '約 35 分鐘', note: '羽田轉車至有明' } },
                            { time: '18:00', item: '有明花園商場晚餐', loc: 'Ariake Garden', toilet: '商場', note: '超大型新商場，內有豐富的美食街。', img: IMG.food, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 10 分鐘', note: 'Small Worlds 步行即可抵達' } },
                            { time: '20:00', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '吃飽早點休息。', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 25 分鐘', note: '有明搭計程車回飯店' } }
                        ],
                        Sat: [
                            { time: '10:30', item: '東京 Joypolis', loc: 'Tokyo Joypolis', toilet: 'DECKS 內', note: 'SEGA 室內樂園，週六放電一整天！', img: IMG.arcade, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 20 分鐘', note: '羽田搭計程車直達台場 DECKS' } },
                            { time: '13:00', item: 'DECKS 午餐與一丁目老街', loc: 'DECKS Tokyo Beach', toilet: '商場', note: '復古雜貨與懷舊氛圍。', img: IMG.street, mapUrl: '', transit: { icon: '🚶', method: '同棟', duration: '約 2 分鐘', note: '' } },
                            { time: '15:30', item: 'DiverCity 逛街與看鋼彈', loc: 'DiverCity', toilet: '商場', note: '轉換陣地，看獨角獸鋼彈變身。', img: IMG.gundam, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 8 分鐘', note: '' } },
                            { time: '18:00', item: '台場海濱夜景晚餐', loc: 'Aqua City', toilet: '商場', note: '看著彩虹大橋夜景用餐。', img: IMG.night_view, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 5 分鐘', note: '' } },
                            { time: '21:00', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 20 分鐘', note: '' } }
                        ],
                        Sun: [
                            { time: '09:00', item: '豐洲千客萬來', loc: 'Toyosu', toilet: '', note: '江戶風美食街！長輩泡免費足湯看海。', img: IMG.toyosu, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 20 分鐘', note: '羽田搭計程車' } },
                            { time: '11:00', item: '豐洲 LaLaport 最後掃貨', loc: 'LaLaport', toilet: '', note: '全家最後採買。', img: IMG.shopping, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 5 分鐘', note: '' } },
                            { time: '12:00', item: '🚕 前往羽田機場', loc: '豐洲 → 羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 20 分鐘', note: '' } }
                        ]
                    }
                },
                D: {
                    id: 'D',
                    type: 'outdoor',
                    title: '方案 D：潮流原宿與神宮森林',
                    subtitle: '原宿 & 澀谷',
                    desc: '把耗費體力的澀谷與原宿拆成兩天！週五征服澀谷地標與唱片行，週六慢搖明治神宮。',
                    recommended: true,
                    chartData: [10, 8, 7, 9, 10, 6],
                    schedule: {
                        Fri: [
                            { time: '15:30', item: '澀谷十字路口 & SHIBUYA SKY', loc: 'Shibuya SKY', toilet: ' SKY 室內有休息座', note: '傍晚時分登上 360 度觀景台，看東京日落與最繁華的十字路口。', img: IMG.shibuya, mapUrl: '', transit: { icon: '🚃', method: '京急轉山手線', duration: '約 35 分鐘', note: '羽田搭京急至品川轉山手線至澀谷' } },
                            { time: '17:30', item: '澀谷唱片行巡禮', loc: 'Tower Records / Disk Union', toilet: 'Tower 內部', note: '日本最大唱片集散地！9層樓 Tower Records 與 Disk Union 皆在步行 3 分內。', img: IMG.records, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 5 分鐘', note: '走過十字路口即抵達' } },
                            { time: '19:00', item: '澀谷晚餐', loc: '澀谷站', toilet: '', note: '選擇極多，從居酒屋到高檔餐廳皆有。', img: IMG.night_view, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 5 分鐘', note: '' } },
                            { time: '21:00', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 30 分鐘', note: '' } }
                        ],
                        Sat: [
                            { time: '10:00', item: '明治神宮', loc: 'Meiji Jingu', toilet: '車站先上', note: '巨型鳥居，長輩散步呼吸芬多精。不受時間壓迫慢慢走。', img: IMG.meiji, mapUrl: '', transit: { icon: '🚃', method: '京急轉山手線', duration: '約 35 分鐘', note: '品川轉山手線到原宿' } },
                            { time: '12:00', item: '表參道午餐與下午茶', loc: 'Omotesando', toilet: '', note: '找間精緻餐廳好好坐下來享受。', img: IMG.food, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 10 分鐘', note: '' } },
                            { time: '14:30', item: '竹下通 / 裏原宿', loc: 'Harajuku', toilet: '', note: '青少年潮流天堂！長輩可在表參道咖啡廳等待。', img: IMG.harajuku, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 5 分鐘', note: '' } },
                            { time: '17:30', item: '六本木夜景或自由活動', loc: '可選', toilet: '', note: '既然澀谷已去過，晚上可安排六本木或新宿自由活動。', img: IMG.roppongi, mapUrl: '', transit: { icon: '🚃', method: '地鐵', duration: '-', note: '' } },
                            { time: '20:30', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 30 分鐘', note: '' } }
                        ],
                        Sun: [
                            { time: '09:00', item: '代代木公園晨散步', loc: 'Yoyogi Park', toilet: '', note: '天氣好超舒服！', img: IMG.yoyogi, mapUrl: '', transit: { icon: '🚃', method: '山手線', duration: '約 35 分鐘', note: '' } },
                            { time: '10:30', item: '最後補貨', loc: '原宿周邊', toilet: '', note: '買齊想要的紀念品。', img: IMG.shopping, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 10 分鐘', note: '' } },
                            { time: '12:00', item: '🚕 前往羽田機場', loc: '原宿 → 羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 35 分鐘', note: '' } }
                        ]
                    }
                },
                E: {
                    id: 'E',
                    type: 'outdoor',
                    title: '方案 E：鋼彈鋼鐵與海風足湯',
                    subtitle: '台場 & 豐洲',
                    desc: '2.5 天的充裕時間，把所有環灣景點深度走完。對體力要求最低的度假選擇！',
                    recommended: true,
                    chartData: [8, 10, 10, 8, 8, 10],
                    schedule: {
                        Fri: [
                            { time: '15:00', item: '豐洲千客萬來', loc: 'Toyosu', toilet: '超新超乾淨', note: '江戶風美食街！長輩泡免費足湯看海，享用新鮮海鮮當下午茶。', img: IMG.toyosu, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 20 分鐘', note: '從羽田搭車直達' } },
                            { time: '18:00', item: '豐洲拉拉寶都晚餐', loc: 'LaLaport', toilet: '', note: '灣區夜景非常舒適。', img: IMG.food, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 5 分鐘', note: '' } },
                            { time: '20:30', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '回程零壓力。', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 20 分鐘', note: '' } }
                        ],
                        Sat: [
                            { time: '10:30', item: '獨角獸鋼彈 1:1 展示', loc: 'DiverCity', toilet: '', note: '整點變身秀！', img: IMG.gundam, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 15 分鐘', note: '' } },
                            { time: '12:00', item: 'DiverCity 午餐', loc: '', toilet: '', note: '各國美食街，選擇超多。', img: IMG.food, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '-', note: '' } },
                            { time: '14:00', item: '鋼彈基地商店', loc: 'DiverCity 7F', toilet: '', note: '青少年掃貨，長輩逛街。', img: IMG.gundam, mapUrl: '', transit: { icon: '🚶', method: '電梯', duration: '-', note: '' } },
                            { time: '16:00', item: '台場海濱公園與 Aqua City', loc: 'Odaiba', toilet: '', note: '遠眺彩虹大橋，在海風中散步。', img: IMG.odaiba, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 8 分鐘', note: '' } },
                            { time: '18:30', item: '台場晚餐看煙火/夜景', loc: '', toilet: '', note: '慢慢吃完搭計程車回飯店。', img: IMG.night_view, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '-', note: '' } },
                            { time: '21:00', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 15 分鐘', note: '' } }
                        ],
                        Sun: [
                            { time: '10:00', item: '泉天空の湯 (飯店內)', loc: '羽田飯店', toilet: '', note: '飯店自帶的天然溫泉，早上泡個湯。', img: IMG.airport, mapUrl: '', transit: { icon: '🚶', method: '直結', duration: '-', note: '' } },
                            { time: '11:00', item: '羽田花園商場買伴手禮', loc: '羽田飯店', toilet: '', note: '直結機場國際線，不用拖行李。', img: IMG.shopping, mapUrl: '', transit: { icon: '🚶', method: '直結', duration: '-', note: '' } },
                            { time: '12:30', item: '🛫 輕鬆報到', loc: '羽田機場', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚶', method: '直結', duration: '-', note: '' } }
                        ]
                    }
                },
                F: {
                    id: 'F',
                    type: 'outdoor',
                    title: '方案 F：下町文化與未來水上船',
                    subtitle: '淺草 & 隅田川',
                    desc: '五六分開踩點晴空塔與淺草寺，完全享受下町風光不趕時間。',
                    recommended: false,
                    chartData: [7, 8, 6, 8, 9, 7],
                    schedule: {
                        Fri: [
                            { time: '15:00', item: '東京晴空塔登頂', loc: 'Skytree', toilet: '商場寬闊', note: '下午剛好人稍微少一點，高空俯瞰東京。', img: IMG.skytree, mapUrl: '', transit: { icon: '🚃', method: '京急轉淺草線', duration: '約 45 分鐘', note: '羽田直達押上站免轉車！' } },
                            { time: '17:30', item: 'Solamachi 商場巡禮', loc: 'Skytree 下方', toilet: '', note: '超多動漫聯名與特色土產店。', img: IMG.shopping, mapUrl: '', transit: { icon: '🚶', method: '電梯', duration: '-', note: '' } },
                            { time: '19:00', item: '晴空塔周邊晚餐', loc: '', toilet: '', note: '', img: IMG.night_view, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '-', note: '' } },
                            { time: '21:00', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚃', method: '淺草線直通', duration: '約 45 分鐘', note: '直達羽田' } }
                        ],
                        Sat: [
                            { time: '10:00', item: '淺草寺 / 雷門', loc: 'Senso-ji', toilet: '觀光中心', note: '早上逛淺草最舒適，長輩求籤小孩拍照。', img: IMG.asakusa, mapUrl: '', transit: { icon: '🚃', method: '京急轉淺草線', duration: '約 40 分鐘', note: '直達淺草站' } },
                            { time: '12:00', item: '淺草午餐與西參道遊戲', loc: '淺草周邊', toilet: '', note: '吃完天丼去玩祭典小遊戲。', img: IMG.food, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 5 分鐘', note: '' } },
                            { time: '14:30', item: '隅田川未來船', loc: '淺草碼頭', toilet: '船上', note: '搭乘 HIMIKO 前往台場，長輩沿途休息看風景。', img: IMG.cruise, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '約 8 分鐘', note: '' } },
                            { time: '16:00', item: '台場海濱與 Aqua City', loc: '台場', toilet: '', note: '抵達台場無縫接軌看夕陽。', img: IMG.odaiba, mapUrl: '', transit: { icon: '🚢', method: '水上巴士', duration: '約 50 分鐘', note: '' } },
                            { time: '18:30', item: '台場晚餐', loc: '', toilet: '', note: '', img: IMG.night_view, mapUrl: '', transit: { icon: '🚶', method: '步行', duration: '-', note: '' } },
                            { time: '20:30', item: '🏨 返回飯店', loc: '羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚕', method: '計程車', duration: '約 20 分鐘', note: '' } }
                        ],
                        Sun: [
                            { time: '09:00', item: '品川水族館', loc: '品川', toilet: '', note: '回國前不跑遠，去品川看秀。', img: IMG.aquarium, mapUrl: '', transit: { icon: '🚃', method: '京急線', duration: '約 15 分鐘', note: '直達品川' } },
                            { time: '12:00', item: '🚕 前往羽田', loc: '品川 → 羽田', toilet: '', note: '', img: IMG.airport, mapUrl: '', transit: { icon: '🚃', method: '京急線', duration: '約 15 分鐘', note: '' } }
                        ]
                    }
                }
            }
        };'''

with open(filename, "r") as f:
    html_content = f.read()

# Replace the block
pattern = r'const reportData = \{.*?\n        \};'
html_content = re.sub(pattern, new_data, html_content, flags=re.DOTALL)

with open(filename, "w") as f:
    f.write(html_content)

print("Data replaced successfully.")
