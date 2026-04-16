import re

filename = "5F-29-PTO-Jap.html"

with open(filename, "r") as f:
    text = f.read()

# 1. Update Headings & Texts
text = text.replace("<title>東京 14H 快閃：家庭專屬行程規劃</title>", "<title>東京 2.5 天：週五請假版</title>")
text = text.replace("東京 14H 快閃<br class=\"md:hidden\">家族決策面板", "東京 2.5 天<br class=\"md:hidden\">週五請假專屬行程")
text = text.replace("實際觀光時間約 <strong class=\"text-amber-300\">14 小時</strong>，每一分鐘都要精準運用！", "實際觀光時間擴展至 <strong class=\"text-amber-300\">2.5 天</strong>，享受更充足悠閒的假期！")
text = text.replace("⏱️ 14H 精華", "⏱️ 2.5 天慢活")
text = text.replace("14H 快閃執行錦囊", "2.5 天悠閒執行錦囊")

# 2. Update Transport Section (Going from Friday evening to Friday morning)
text = text.replace("📍 去程：週五 5/29", "📍 早班去程：週五 5/29")
old_table = """<table class="w-full text-sm">
                                <thead>
                                    <tr class="border-b border-sky-200">
                                        <th class="text-left py-2 px-3 text-sky-800">航班</th>
                                        <th class="text-left py-2 px-3 text-sky-800">松山起飛</th>
                                        <th class="text-left py-2 px-3 text-sky-800">需到松山</th>
                                        <th class="text-left py-2 px-3 text-sky-800">需到台北車站</th>
                                        <th class="text-left py-2 px-3 text-sky-800 font-black">🚄 台中最晚出發</th>
                                        <th class="text-left py-2 px-3 text-sky-800">抵達羽田</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="border-b border-sky-100">
                                        <td class="py-2.5 px-3 font-medium">BR190 長榮</td>
                                        <td class="py-2.5 px-3">16:20</td>
                                        <td class="py-2.5 px-3">14:20</td>
                                        <td class="py-2.5 px-3">14:00</td>
                                        <td class="py-2.5 px-3 font-black text-sky-900 text-base">🕐 13:00</td>
                                        <td class="py-2.5 px-3 text-stone-500">20:20（日本）</td>
                                    </tr>
                                    <tr class="bg-emerald-50 border border-emerald-200 rounded">
                                        <td class="py-2.5 px-3 font-bold text-emerald-800">CI222 華航 <span class="badge-recommended">最晚</span></td>
                                        <td class="py-2.5 px-3 font-bold text-emerald-800">18:05</td>
                                        <td class="py-2.5 px-3">16:05</td>
                                        <td class="py-2.5 px-3">15:45</td>
                                        <td class="py-2.5 px-3 font-black text-emerald-900 text-base">🕐 14:50</td>
                                        <td class="py-2.5 px-3 text-stone-500">22:05（日本）</td>
                                    </tr>
                                </tbody>
                            </table>"""

new_table = """<table class="w-full text-sm">
                                <thead>
                                    <tr class="border-b border-sky-200">
                                        <th class="text-left py-2 px-3 text-sky-800">航班</th>
                                        <th class="text-left py-2 px-3 text-sky-800">松山起飛</th>
                                        <th class="text-left py-2 px-3 text-sky-800">需到松山</th>
                                        <th class="text-left py-2 px-3 text-sky-800">需到台北車站</th>
                                        <th class="text-left py-2 px-3 text-sky-800 font-black">🚄 台中推薦出發</th>
                                        <th class="text-left py-2 px-3 text-sky-800">抵達羽田</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="bg-emerald-50 border border-emerald-200 rounded">
                                        <td class="py-2.5 px-3 font-bold text-emerald-800">CI220 華航 <span class="badge-recommended">✨ 舒適早班</span></td>
                                        <td class="py-2.5 px-3 font-bold text-emerald-800">09:00</td>
                                        <td class="py-2.5 px-3">07:00</td>
                                        <td class="py-2.5 px-3">06:30</td>
                                        <td class="py-2.5 px-3 font-black text-emerald-900 text-base">🕐 05:40 (或首班高鐵)</td>
                                        <td class="py-2.5 px-3 text-stone-500">13:10（日本）</td>
                                    </tr>
                                    <tr class="border-b border-sky-100">
                                        <td class="py-2.5 px-3 font-medium">BR192 長榮</td>
                                        <td class="py-2.5 px-3">07:20</td>
                                        <td class="py-2.5 px-3">05:20</td>
                                        <td class="py-2.5 px-3">N/A</td>
                                        <td class="py-2.5 px-3 font-black text-sky-900 text-base">🚗 03:00 (需包車/自駕)</td>
                                        <td class="py-2.5 px-3 text-stone-500">11:35（日本）</td>
                                    </tr>
                                </tbody>
                            </table>"""
text = text.replace(old_table, new_table)

# 3. Update Visual Timeline to match CI220
old_timeline_str = "▼ 以推薦航班 BR190 為例的時間軸"
new_timeline_str = "▼ 以舒適早班 CI220 為例的時間軸"
text = text.replace(old_timeline_str, new_timeline_str)

old_timeline = """<div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🚄</div>
                            <p class="font-bold text-sm mt-3">台中高鐵站</p>
                            <p class="text-xs text-stone-400 mt-1">最晚 13:00</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🏙️</div>
                            <p class="font-bold text-sm mt-3">台北車站</p>
                            <p class="text-xs text-stone-400 mt-1">~13:50 抵達</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🛫</div>
                            <p class="font-bold text-sm mt-3">松山機場</p>
                            <p class="text-xs text-stone-400 mt-1">14:20 報到</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">✈️</div>
                            <p class="font-bold text-sm mt-3">BR190 起飛</p>
                            <p class="text-xs text-stone-400 mt-1">16:20</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🛬</div>
                            <p class="font-bold text-sm mt-3">羽田機場</p>
                            <p class="text-xs text-stone-400 mt-1">20:20（日本）</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🏨</div>
                            <p class="font-bold text-sm mt-3">入住飯店</p>
                            <p class="text-xs text-stone-400 mt-1">~21:00 休息</p>
                        </div>"""

new_timeline = """<div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🚄</div>
                            <p class="font-bold text-sm mt-3">首班高鐵或包車</p>
                            <p class="text-xs text-stone-400 mt-1">05:40 台中</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🏙️</div>
                            <p class="font-bold text-sm mt-3">台北車站</p>
                            <p class="text-xs text-stone-400 mt-1">~06:30 抵達</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🛫</div>
                            <p class="font-bold text-sm mt-3">松山機場</p>
                            <p class="text-xs text-stone-400 mt-1">07:00 報到</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">✈️</div>
                            <p class="font-bold text-sm mt-3">CI220 起飛</p>
                            <p class="text-xs text-stone-400 mt-1">09:00</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🛬</div>
                            <p class="font-bold text-sm mt-3">羽田機場</p>
                            <p class="text-xs text-stone-400 mt-1">13:10（日本）</p>
                        </div>
                        <div class="timeline-connector"></div>
                        <div class="timeline-step min-w-[90px]">
                            <div class="icon-circle">🗼</div>
                            <p class="font-bold text-sm mt-3">放行李 / 觀光</p>
                            <p class="text-xs text-stone-400 mt-1">15:00 開始</p>
                        </div>"""
text = text.replace(old_timeline, new_timeline)

# Flight options block update
old_flight_options = """<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="flight-option recommended">
                            <div class="flex items-center justify-between mb-2">
                                <span class="font-bold text-lg text-emerald-800">BR190 長榮航空</span>
                                <span class="badge-recommended">✨ 推薦</span>
                            </div>
                            <div class="flex items-center gap-4 text-stone-600">
                                <div>
                                    <p class="text-2xl font-black text-stone-800">16:20</p>
                                    <p class="text-xs">松山 TSA</p>
                                </div>
                                <div class="flex-1 text-center">
                                    <p class="text-xs text-stone-400">── ✈️ 約 3hr ──</p>
                                </div>
                                <div>
                                    <p class="text-2xl font-black text-stone-800">20:20</p>
                                    <p class="text-xs">羽田 HND（日本時間）</p>
                                </div>
                            </div>
                            <p class="text-sm text-emerald-700 mt-3">較早到達，可在飯店周邊吃晚餐、逛便利商店採買明日物資。</p>
                        </div>
                        <div class="flight-option">
                            <div class="flex items-center justify-between mb-2">
                                <span class="font-bold text-lg text-stone-700">CI222 中華航空</span>
                            </div>
                            <div class="flex items-center gap-4 text-stone-600">
                                <div>
                                    <p class="text-2xl font-black text-stone-800">18:05</p>
                                    <p class="text-xs">松山 TSA</p>
                                </div>
                                <div class="flex-1 text-center">
                                    <p class="text-xs text-stone-400">── ✈️ 約 3hr ──</p>
                                </div>
                                <div>
                                    <p class="text-2xl font-black text-stone-800">22:05</p>
                                    <p class="text-xs">羽田 HND（日本時間）</p>
                                </div>
                            </div>
                            <p class="text-sm text-stone-500 mt-3">適合無法提早出發者，但到達較晚，直接回飯店休息。</p>
                        </div>
                    </div>"""
new_flight_options = """<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="flight-option recommended">
                            <div class="flex items-center justify-between mb-2">
                                <span class="font-bold text-lg text-emerald-800">CI220 中華航空</span>
                                <span class="badge-recommended">✨ 舒適早班</span>
                            </div>
                            <div class="flex items-center gap-4 text-stone-600">
                                <div>
                                    <p class="text-2xl font-black text-stone-800">09:00</p>
                                    <p class="text-xs">松山 TSA</p>
                                </div>
                                <div class="flex-1 text-center">
                                    <p class="text-xs text-stone-400">── ✈️ 約 3hr ──</p>
                                </div>
                                <div>
                                    <p class="text-2xl font-black text-stone-800">13:10</p>
                                    <p class="text-xs">羽田 HND（日本時間）</p>
                                </div>
                            </div>
                            <p class="text-sm text-emerald-700 mt-3">不需摸黑出門，抵達時間漂亮，擁有完整的週五傍晚與夜晚。</p>
                        </div>
                        <div class="flight-option">
                            <div class="flex items-center justify-between mb-2">
                                <span class="font-bold text-lg text-stone-700">BR192 長榮航空</span>
                            </div>
                            <div class="flex items-center gap-4 text-stone-600">
                                <div>
                                    <p class="text-2xl font-black text-stone-800">07:20</p>
                                    <p class="text-xs">松山 TSA</p>
                                </div>
                                <div class="flex-1 text-center">
                                    <p class="text-xs text-stone-400">── ✈️ 約 3hr ──</p>
                                </div>
                                <div>
                                    <p class="text-2xl font-black text-stone-800">11:35</p>
                                    <p class="text-xs">羽田 HND（日本時間）</p>
                                </div>
                            </div>
                            <p class="text-sm text-stone-500 mt-3">時間最大化選擇，中午前入住。但需包車或自駕於凌晨 3 點從台中出發。</p>
                        </div>
                    </div>"""
text = text.replace(old_flight_options, new_flight_options)

# Remove the "方案 B: 5/30 開車" and replace with something minimal or strip it
# The simplest is simply to leave it or strip it. Let's delete it so it's clean via regex
import re
text = re.sub(r'<!-- 分隔線 -->.*?<!-- Section 2: 天氣選擇 -->', '<!-- Section 2: 天氣選擇 -->', text, flags=re.DOTALL)

# 4. Modify Tabs in UI
old_tabs = """<div class="flex border-b border-stone-200 mb-6">
                            <button id="tab-sat" onclick="switchDay('Sat')" class="py-2 px-6 text-lg font-medium text-stone-500 hover:text-stone-800 focus:outline-none tab-active">
                                🔥 週六全天
                            </button>
                            <button id="tab-sun" onclick="switchDay('Sun')" class="py-2 px-6 text-lg font-medium text-stone-500 hover:text-stone-800 focus:outline-none">
                                ☀️ 週日上午
                            </button>
                        </div>"""
new_tabs = """<div class="flex border-b border-stone-200 mb-6 flex-wrap">
                            <button id="tab-fri" onclick="switchDay('Fri')" class="py-2 px-6 text-lg font-medium text-stone-500 hover:text-stone-800 focus:outline-none tab-active">
                                ✨ 週五下午
                            </button>
                            <button id="tab-sat" onclick="switchDay('Sat')" class="py-2 px-6 text-lg font-medium text-stone-500 hover:text-stone-800 focus:outline-none">
                                🔥 週六全天
                            </button>
                            <button id="tab-sun" onclick="switchDay('Sun')" class="py-2 px-6 text-lg font-medium text-stone-500 hover:text-stone-800 focus:outline-none">
                                ☀️ 週日上午
                            </button>
                        </div>"""
text = text.replace(old_tabs, new_tabs)

# 5. Modify switchDay Javascript
old_switchDay = """function switchDay(day) {
            currentDayTab = day;
            document.getElementById('tab-sat').classList.remove('tab-active');
            document.getElementById('tab-sun').classList.remove('tab-active');

            if (day === 'Sat') document.getElementById('tab-sat').classList.add('tab-active');
            if (day === 'Sun') document.getElementById('tab-sun').classList.add('tab-active');

            renderSchedule();
        }"""
new_switchDay = """function switchDay(day) {
            currentDayTab = day;
            document.getElementById('tab-fri').classList.remove('tab-active');
            document.getElementById('tab-sat').classList.remove('tab-active');
            document.getElementById('tab-sun').classList.remove('tab-active');

            if (day === 'Fri') document.getElementById('tab-fri').classList.add('tab-active');
            if (day === 'Sat') document.getElementById('tab-sat').classList.add('tab-active');
            if (day === 'Sun') document.getElementById('tab-sun').classList.add('tab-active');

            renderSchedule();
        }"""
text = text.replace(old_switchDay, new_switchDay)

old_selectPlan_tab = """document.getElementById('tab-sat').classList.add('tab-active');
            document.getElementById('tab-sun').classList.remove('tab-active');"""
new_selectPlan_tab = """document.getElementById('tab-fri').classList.add('tab-active');
            document.getElementById('tab-sat').classList.remove('tab-active');
            document.getElementById('tab-sun').classList.remove('tab-active');"""
text = text.replace(old_selectPlan_tab, new_selectPlan_tab)

old_selectPlan_tab2 = """currentDayTab = 'Sat';"""
new_selectPlan_tab2 = """currentDayTab = 'Fri';"""
text = text.replace(old_selectPlan_tab2, new_selectPlan_tab2)

# 6. We rewrite `reportData` completely down below.
with open(filename, "w") as f:
    f.write(text)

print("Template setup successfully!")
