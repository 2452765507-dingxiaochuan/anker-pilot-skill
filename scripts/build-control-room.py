#!/usr/bin/env python3
from pathlib import Path
import re, html

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'website' / 'prompts.html'

CSS = r'''
:root{--ink:#111318;--sub:#5e6675;--line:#dfe3e9;--bg:#f5f6f8;--card:#fff;--blue:#1267e5;--navy:#071c36;--soft:#eaf2ff;--green:#087e53;--orange:#b75500;--shadow:0 12px 40px rgba(10,24,50,.07)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;color:var(--ink);background:#fff;line-height:1.72}a{color:inherit}.wrap{max-width:1220px;margin:auto;padding:0 28px}
header{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.91);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}.nav{height:62px;display:flex;align-items:center;gap:26px}.brand{font-weight:850;color:var(--navy);white-space:nowrap}.brand i{font-style:normal;color:var(--blue)}.navlinks{display:flex;gap:14px;overflow:auto;scrollbar-width:none}.navlinks a{text-decoration:none;font-size:13px;color:var(--sub);white-space:nowrap;padding:7px 9px;border-radius:8px}.navlinks a:hover{background:var(--bg);color:var(--blue)}
.hero{background:radial-gradient(circle at 75% 25%,#d9e9ff 0,transparent 34%),linear-gradient(150deg,#f8fbff,#fff 55%);border-bottom:1px solid var(--line);padding:76px 0 58px}.eyebrow{display:inline-flex;padding:6px 11px;border-radius:999px;background:var(--soft);color:var(--blue);font-size:12px;font-weight:800;letter-spacing:.5px}.hero h1{font-size:48px;line-height:1.12;max-width:900px;margin:18px 0 15px;letter-spacing:-1.6px}.hero p{font-size:17px;color:var(--sub);max-width:830px;margin:0}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:34px}.stat{padding:18px;border:1px solid var(--line);border-radius:14px;background:rgba(255,255,255,.82)}.stat b{font-size:23px;display:block}.stat span{font-size:12.5px;color:var(--sub)}
.toolbar{position:sticky;top:62px;z-index:90;background:#fff;border-bottom:1px solid var(--line);padding:12px 0}.toolrow{display:flex;gap:10px;align-items:center}.search{flex:1;min-width:220px;border:1px solid var(--line);border-radius:10px;padding:10px 13px;font-size:14px}.pill{border:1px solid var(--line);border-radius:999px;padding:8px 12px;background:#fff;font-size:12px;cursor:pointer}.pill:hover{border-color:#aab6c8}
.route{padding:42px 0}.route h2,.section h2{font-size:27px;letter-spacing:-.5px}.flow{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}.step{padding:16px;border-radius:13px;background:var(--bg);border:1px solid var(--line)}.step b{display:block;color:var(--blue);font-size:12px;margin-bottom:4px}.step span{font-size:13px;color:var(--sub)}
.section,.scenario{padding:50px 0;border-top:1px solid var(--line)}.sec-title{display:flex;align-items:flex-start;gap:14px;margin-bottom:20px}.num{min-width:42px;height:42px;padding:0 8px;border-radius:12px;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:850;flex:none}.sec-title h2{margin:2px 0 3px}.sec-title p{margin:0;color:var(--sub);font-size:14px}
.prompt-stack{display:grid;gap:15px}.prompt-card{border:1px solid var(--line);border-radius:15px;overflow:hidden;background:var(--card);box-shadow:0 2px 10px rgba(15,30,60,.025)}.pc-head{padding:13px 16px;background:#f8f9fb;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:12px}.pc-head h4{margin:0;font-size:15px}.pc-head span{font-size:11px;color:var(--sub)}button.copy{border:0;background:var(--navy);color:#fff;padding:7px 13px;border-radius:8px;font-weight:750;cursor:pointer}.copy.done{background:var(--green)}pre{white-space:pre-wrap;word-break:break-word;margin:0;padding:18px;font-family:"SFMono-Regular",Consolas,monospace;font-size:13.3px;line-height:1.75;color:#21252d;max-height:620px;overflow:auto}
details{margin:12px 0 20px;border:1px solid var(--line);border-radius:14px;background:#fafbfc}summary{cursor:pointer;font-weight:750;padding:14px 17px}.case-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:0 14px 14px}.case-card{text-decoration:none;border:1px solid var(--line);background:#fff;border-radius:12px;padding:14px;min-height:118px;transition:.15s}.case-card:hover{transform:translateY(-1px);box-shadow:var(--shadow);border-color:#bfd2ed}.case-card b{font-size:13.5px}.case-card p{font-size:12.5px;color:var(--sub);margin:7px 0}.case-card span{font-size:11px;color:var(--blue)}
.meta-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:0 0 16px}.meta-box{padding:13px 15px;border:1px solid var(--line);border-radius:12px;background:#fbfcfe}.meta-box b{font-size:12px;color:var(--blue);display:block;margin-bottom:4px}.meta-box p{font-size:13px;color:var(--sub);margin:0}.quicknav{display:grid;grid-template-columns:repeat(4,1fr);gap:9px;margin:20px 0 4px}.quicknav a{text-decoration:none;padding:12px 13px;border:1px solid var(--line);border-radius:12px;background:#fff}.quicknav b{display:block;font-size:13px;color:var(--navy)}.quicknav span{font-size:11.5px;color:var(--sub)}.methods{display:grid;grid-template-columns:1fr 1fr;gap:12px}.method{padding:18px;border:1px solid var(--line);border-radius:14px}.method b{display:block;margin-bottom:6px}.method p{font-size:13px;color:var(--sub)}.links{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}.links a{text-decoration:none;border:1px solid var(--line);padding:8px 10px;border-radius:9px;font-size:12px;color:var(--blue)}
.hidden{display:none!important}.notice{padding:15px 17px;background:#fff8e9;border:1px solid #efdca7;color:#624300;border-radius:12px;font-size:13px;margin-top:18px}.meta-line{font-size:12px;color:var(--sub);margin:6px 0 18px}.source-note{font-size:12px;color:var(--sub);padding:0 17px 14px}footer{padding:45px 0 70px;border-top:1px solid var(--line);color:var(--sub);font-size:13px}
@media(max-width:900px){.hero h1{font-size:36px}.quicknav{grid-template-columns:repeat(2,1fr)}.meta-grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}.flow{grid-template-columns:repeat(3,1fr)}.case-grid{grid-template-columns:1fr 1fr}.methods{grid-template-columns:1fr}.navlinks{display:none}}
@media(max-width:560px){.wrap{padding:0 16px}.hero{padding:50px 0 38px}.hero h1{font-size:31px}.flow{grid-template-columns:1fr 1fr}.case-grid{grid-template-columns:1fr}.toolrow{flex-wrap:wrap}}
'''

def read(p): return (ROOT / p).read_text(encoding='utf-8')

def esc(s): return html.escape(s, quote=True)

def title_from_h1(text):
    m=re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else ''

def first_code(text):
    m=re.search(r'```text\n(.*?)\n```', text, re.S)
    return m.group(1).strip() if m else ''

def sections(text):
    out=[]
    for m in re.finditer(r'^##\s+(.+?)\n(.*?)(?=^##\s+|\Z)', text, re.M|re.S):
        heading=m.group(1).strip(); body=m.group(2)
        cm=re.search(r'```text\n(.*?)\n```', body, re.S)
        if cm: out.append((heading, cm.group(1).strip()))
    return out

def prompt_card(title, body):
    return f'<article class="prompt-card searchable"><div class="pc-head"><div><h4>{esc(title)}</h4><span>可复制</span></div><button class="copy">复制</button></div><pre>{esc(body)}</pre></article>'

def case_items(text):
    items=[]
    blocks=re.split(r'(?=^##\s+)', text, flags=re.M)
    for b in blocks:
        m=re.match(r'^##\s+(.+?)\n', b)
        if not m: continue
        title=m.group(1).strip()
        if any(k in title for k in ['检查','原则','来源','用法','README']): continue
        urls=re.findall(r'https?://[^\s)]+', b)
        if not urls: continue
        url=urls[0].rstrip('.,;')
        trans=re.search(r'- \*\*可迁移\*\*[:：]\s*(.+)', b)
        if trans: desc=trans.group(1).strip()
        else:
            bullets=[x.strip()[2:].strip() for x in b.splitlines() if x.strip().startswith('- ') and '来源' not in x]
            desc=bullets[0] if bullets else '查看原始案例与方法。'
        items.append((title, desc, url))
    return items

def case_grid(path):
    items=case_items(read(path))
    cards=''.join(f'<a class="case-card" href="{esc(u)}" target="_blank" rel="noopener"><b>{esc(t)}</b><p>{esc(d)}</p><span>原始案例 ↗</span></a>' for t,d,u in items)
    return f'<details open><summary>案例素材包 · {len(items)} 个研究节点</summary><div class="case-grid">{cards}</div><div class="source-note">案例用于迁移机制；品牌/平台/供应商案例中的效果数据保留原始来源口径。完整来源分类见 references/scenario-case-packs/source-register.csv。</div></details>'

def section_html(id_, num, title, desc, cards, extra=''):
    return f'<section id="{id_}" class="section searchable"><div class="sec-title"><div class="num">{esc(num)}</div><div><h2>{esc(title)}</h2><p>{esc(desc)}</p></div></div>{extra}<div class="prompt-stack">{cards}</div></section>'

def plain_section(text, heading):
    m=re.search(r'^##\s+'+re.escape(heading)+r'\s*\n(.*?)(?=^##\s+|\Z)', text, re.M|re.S)
    if not m: return ''
    body=re.sub(r'```.*?```','',m.group(1),flags=re.S).strip()
    body=re.sub(r'^[-*]\s+','',body,flags=re.M)
    return ' '.join(x.strip() for x in body.splitlines() if x.strip())

def bullet_section(text, heading):
    m=re.search(r'^##\s+'+re.escape(heading)+r'\s*\n(.*?)(?=^##\s+|\Z)', text, re.M|re.S)
    if not m: return []
    return [x.strip()[2:].strip() for x in m.group(1).splitlines() if x.strip().startswith('- ')]

def scenario_html(idx, path, casepath, title, desc):
    text=read(path)
    ss=sections(text)
    cards=''.join(prompt_card(h,b) for h,b in ss)
    use=plain_section(text,'适用题型')
    inputs=plain_section(text,'最少需要的输入') or plain_section(text,'前置原则')
    avoids=bullet_section(text,'注意避免')
    meta=''
    if use or inputs:
        meta='<div class="meta-grid">'
        if use: meta+=f'<div class="meta-box"><b>什么时候用</b><p>{esc(use)}</p></div>'
        if inputs: meta+=f'<div class="meta-box"><b>开始前先准备</b><p>{esc(inputs)}</p></div>'
        meta+='</div>'
    avoid_html=''
    if avoids:
        lis=''.join(f'<li>{esc(x)}</li>' for x in avoids)
        avoid_html=f'<details><summary>注意避免</summary><div class="source-note"><ul>{lis}</ul></div></details>'
    open_attr=' open' if idx=='3a' else ''
    cases=case_grid(casepath).replace('<details open>',f'<details{open_attr}>')
    return f'<section id="{idx}" class="scenario searchable"><div class="sec-title"><div class="num">{idx.upper()}</div><div><h2>{esc(title)}</h2><p>{esc(desc)}</p></div></div>{meta}{cases}<div class="prompt-stack">{cards}</div>{avoid_html}</section>'

# Build core cards
expert=read('prompts/00-anker-expert-mode.md'); perf=read('prompts/00A-performance-mode.md')
start_cards=prompt_card('0｜安克业务专家模式', first_code(expert))+prompt_card('0A｜Claude 高性能作战模式', first_code(perf))
general=''.join(prompt_card(h,b) for h,b in sections(read('prompts/01-general-core.md')))
comms=''.join(prompt_card(h,b) for h,b in sections(read('prompts/02-communications-core.md')))
delivery=''.join(prompt_card(h,b) for h,b in sections(read('prompts/03-delivery-modules.md')))
final=''.join(prompt_card(h,b) for h,b in sections(read('prompts/04-final-review.md')))

scenarios=[
('3a','scenarios/01-offline-experience.md','references/scenario-case-packs/01-offline-experience-cases.md','线下体验空间 / 门店 / 品牌体验','旗舰店、快闪、展厅、EBC · 案例迁移 + Demo + 运营 + 经营闭环'),
('3b','scenarios/02-overseas-gtm.md','references/scenario-case-packs/02-overseas-gtm-cases.md','海外新品 GTM','市场进入、定位、首批口碑、渠道接力、本地化、经济性'),
('3c','scenarios/03-ai-content.md','references/scenario-case-packs/03-ai-content-cases.md','AI 内容生产 / 本地化','内容供应链、母资产、多平台变体、视觉、本地化、QC'),
('3d','scenarios/04-integrated-campaign.md','references/scenario-case-packs/04-integrated-campaign-cases.md','整合营销 / 品牌战役','机会洞察、Big Idea、参与机制、渠道接力、资产与衡量'),
('3e','scenarios/05-pr-media.md','references/scenario-case-packs/05-pr-media-cases.md','PR / 媒体 / 发布会','新闻价值、Media Kit、发言人、记者旅程、Earned Media'),
('3f','scenarios/06-social-growth.md','references/scenario-case-packs/06-social-growth-cases.md','社媒增长 / 内容矩阵','数据诊断、内容世界观、Creator/UGC、增长循环'),
('3g','scenarios/07-crisis-trust.md','references/scenario-case-packs/07-crisis-trust-cases.md','舆情 / 危机 / 信任修复','事实中心、行动节奏、证据更新、补救与恢复'),
('3h','scenarios/08-tech-to-human.md','references/scenario-case-packs/08-tech-to-human-cases.md','科技传播 / 技术转译','技术事实、用户价值、分层表达、Proof Design、FAQ')]
scenario_blocks=''.join(scenario_html(*x) for x in scenarios)

methods='''<section id="methods" class="section searchable"><div class="sec-title"><div class="num">+</div><div><h2>外部 Skill 方法内化</h2><p>核心能力已写进 V6；第三方安装只作为可选增强</p></div></div><div class="methods">
<div class="method"><b>Anthropic Skill Creator</b><p>渐进式加载、清晰触发、测试题与迭代。用于控制 3 小时上下文并让专项按需加载。</p></div>
<div class="method"><b>Anthropic Frontend Design</b><p>设计从具体 brief 和内容出发，做明确的版式、字体和视觉判断，减少模板化 UI。</p></div>
<div class="method"><b>Anthropic Webapp Testing</b><p>网页完成前实际打开、操作、看 console/交互/移动端；有 Playwright 时优先自动化验证。</p></div>
<div class="method"><b>Superpowers · MIT</b><p>独立任务并行、先构思再执行、计划边界清楚、完成前用新鲜证据验证。</p></div>
<div class="method"><b>Humanizer-zh · MIT</b><p>保留事实、确定程度与作者判断，重点处理空话、重复、模板句和过度工整。</p></div>
<div class="method"><b>V6 自测集</b><p>evals/test-cases.json 提供代表题与验收项，用于检查 Skill 是否真正提高结果。</p></div>
</div><div class="links"><a href="https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md" target="_blank">Skill Creator ↗</a><a href="https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md" target="_blank">Frontend Design ↗</a><a href="https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md" target="_blank">Webapp Testing ↗</a><a href="https://github.com/obra/superpowers" target="_blank">Superpowers ↗</a><a href="https://github.com/op7418/Humanizer-zh" target="_blank">Humanizer-zh ↗</a></div></section>'''

JS = r'''
function jump(id){document.getElementById(id)?.scrollIntoView({behavior:'smooth'})}
function fallbackCopy(text){const ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.focus();ta.select();try{document.execCommand('copy')}catch(e){}document.body.removeChild(ta)}
document.addEventListener('click',e=>{const b=e.target.closest('button.copy');if(!b)return;const t=b.closest('.prompt-card').querySelector('pre').innerText;const old=b.textContent;b.textContent='已复制 ✓';b.classList.add('done');setTimeout(()=>{b.textContent=old;b.classList.remove('done')},1300);if(navigator.clipboard?.writeText){navigator.clipboard.writeText(t).catch(()=>fallbackCopy(t))}else fallbackCopy(t)});
const q=document.getElementById('q');q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();document.querySelectorAll('.searchable').forEach(el=>{if(el.classList.contains('section')||el.classList.contains('scenario'))return;el.classList.toggle('hidden',v && !el.innerText.toLowerCase().includes(v))})});
'''

parts = [
'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Anker Pilot V6 · Prompt Control Room</title><style>', CSS, '</style></head><body>',
'<header><div class="wrap nav"><div class="brand">Anker <i>Pilot V6</i></div><nav class="navlinks"><a href="#start">0 启动</a><a href="#general">1 通用</a><a href="#comms">2 传播</a><a href="#3a">3A–H 专项</a><a href="#delivery">4 交付</a><a href="#final">5 验证</a><a href="#methods">Skill 方法</a><a href="company-intelligence.html">公司情报 ↗</a></nav></div></header>',
'<section class="hero"><div class="wrap"><span class="eyebrow">ANKER AI PILOT · DEEP SCENARIO SYSTEM</span><h1>案例先研究，方案再生长。<br>每个专项都有推导、边界和验收。</h1><p>V6 把 3A–3H 做成完整专业包：成熟案例负责提供可迁移机制，Prompt 负责完成专业推导，成功标准负责把控质量；同时内化并行研究、渐进式上下文、反模板设计、自然语言编辑与真实验证，让 3 小时更多用于真正影响成绩的判断。</p><div class="stats"><div class="stat"><b>8</b><span>深度专项包</span></div><div class="stat"><b>8</b><span>外链案例研究包</span></div><div class="stat"><b>4+3</b><span>通用 + 传播核心 Prompt</span></div><div class="stat"><b>6</b><span>代表性 Skill 自测题</span></div></div><div class="notice">路线：真题先走 0→1；涉及传播再加 2；选择 1 个主专项，必要时叠加 1 个辅助专项。案例只迁移机制，不照搬品牌形式。题目要求什么交付物，再调用对应交付模块。</div></div></section>',
'<div class="toolbar"><div class="wrap toolrow"><input id="q" class="search" placeholder="搜索：GTM / 空间 / KOL / Demo / KPI / 危机 / 本地化…"><button class="pill" onclick="jump(\'3a\')">专项</button><button class="pill" onclick="jump(\'delivery\')">交付</button><button class="pill" onclick="jump(\'final\')">终检</button></div></div>',
'<main class="wrap"><section class="route"><h2>考试路线</h2><div class="flow"><div class="step"><b>0</b>公司情报<span>只加载真题相关资料</span></div><div class="step"><b>0A</b>高性能<span>并行、阶段快照、验证</span></div><div class="step"><b>1</b>通用主干<span>审题→证据→策略→交付</span></div><div class="step"><b>2</b>传播加固<span>人群→主张→传播系统</span></div><div class="step"><b>3</b>专项深研<span>案例→专业机制→验收</span></div><div class="step"><b>4–5</b>成品验证<span>视觉/文字/文件实测</span></div></div><div class="quicknav"><a href="#3a"><b>3A · 线下体验</b><span>空间 / 门店 / Demo / 运营</span></a><a href="#3b"><b>3B · 海外 GTM</b><span>上市 / 市场进入 / 本地化</span></a><a href="#3c"><b>3C · AI 内容</b><span>内容工厂 / 多平台 / QC</span></a><a href="#3d"><b>3D · 整合营销</b><span>Campaign / Big Idea / 参与</span></a><a href="#3e"><b>3E · PR 媒体</b><span>发布会 / 新闻 / Media Kit</span></a><a href="#3f"><b>3F · 社媒增长</b><span>内容矩阵 / Creator / UGC</span></a><a href="#3g"><b>3G · 危机信任</b><span>事实 / 响应 / 恢复</span></a><a href="#3h"><b>3H · 科技传播</b><span>技术转译 / Proof / Demo</span></a></div></section>',
section_html('start','0','启动底座','安克业务专家 + Claude 高性能作战模式',start_cards),
section_html('general','1','任意题型通用主干','先把业务问题做对，再决定需要什么专业能力',general),
section_html('comms','2','传播推广专业加固','受众变化、品牌主张、创意、内容、媒体、预算与指标',comms),
scenario_blocks,
section_html('delivery','4','交付模块','方案、HTML / Demo、数据看板、视觉与内容样稿',delivery),
section_html('final','5','最终验证','建设性压力测试 + 事实 / 文件 / 页面实际检查',final),
methods,
'</main><footer><div class="wrap">V6 · 公司情报核验截止 2026-10-11。外部案例和高动态业务信息在考试当天按需刷新。网页由 <code>scripts/build-control-room.py</code> 从 Prompt / Scenario 源文件生成，避免网页与 Skill 内容漂移。</div></footer><script>', JS, '</script></body></html>'
]
body=''.join(parts)
OUT.write_text(body,encoding='utf-8')
print(f'Wrote {OUT}')
print('prompt cards', body.count('class="prompt-card searchable"'))
print('case cards', body.count('class="case-card"'))
