<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>فيت سمارت AI — المدرب وحاسبة السعرات الذكية</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=Cairo:wght@400;500;600;700;800;900&family=Almarai:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
  :root {
    --bg-main: #FFFFFF;
    --bg-card: #FFFFFF;
    --bg-subtle: #F8F9FA;
    --bg-muted: #F1F5F9;
    --border: #E2E8F0;
    --border-light: #EDF2F7;
    
    --text-primary: #1E293B;
    --text-secondary: #64748B;
    --text-muted: #94A3B8;

    --green-lime: #22C55E;
    --green-lime-glow: rgba(34, 197, 94, 0.28);
    --green-soft: #DCFCE7;
    
    --orange-fire: #FF6B00;
    --orange-glow: rgba(255, 107, 0, 0.25);
    --orange-soft: #FFEDD5;

    --blue-sport: #0284C7;
    --blue-soft: #E0F2FE;

    --gold-pro: #F59E0B;
    --gold-soft: #FEF3C7;

    --shadow-soft: 0 10px 30px -8px rgba(15, 23, 42, 0.08);
    --shadow-card: 0 4px 20px -2px rgba(15, 23, 42, 0.06);
    --shadow-floating: 0 16px 40px -10px rgba(15, 23, 42, 0.12);

    --radius-xl: 24px;
    --radius-lg: 18px;
    --radius-md: 14px;
    --radius-pill: 9999px;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
  }

  body {
    font-family: 'Cairo', system-ui, -apple-system, sans-serif;
    background-color: var(--bg-subtle);
    color: var(--text-primary);
    min-height: 100vh;
    padding-bottom: 110px;
    overflow-x: hidden;
  }

  /* ===== الهيدر العلوي النقي ===== */
  header {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border-light);
    position: sticky;
    top: 0;
    z-index: 40;
    padding: 12px 18px;
  }
  .header-inner {
    max-width: 480px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .user-badge {
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
  }
  .avatar-wrap {
    position: relative;
    width: 44px;
    height: 44px;
    border-radius: var(--radius-pill);
    background: linear-gradient(135deg, #E2E8F0, #F8F9FA);
    border: 2px solid #FFFFFF;
    box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    color: var(--green-lime);
    font-size: 1.1rem;
  }
  .pro-badge {
    position: absolute;
    bottom: -3px;
    left: -4px;
    background: linear-gradient(135deg, #F59E0B, #D97706);
    color: #FFFFFF;
    font-size: 0.55rem;
    font-weight: 900;
    padding: 2px 5px;
    border-radius: var(--radius-pill);
    border: 1.5px solid #FFFFFF;
    letter-spacing: 0.5px;
    box-shadow: 0 2px 6px rgba(217, 119, 6, 0.4);
    animation: goldShine 3s infinite ease-in-out;
  }
  @keyframes goldShine {
    0%, 100% { transform: scale(1); filter: brightness(1); }
    50% { transform: scale(1.08); filter: brightness(1.2); }
  }
  .user-meta h1 {
    font-size: 0.96rem;
    font-weight: 800;
    line-height: 1.2;
    color: var(--text-primary);
  }
  .user-meta p {
    font-size: 0.68rem;
    color: var(--text-secondary);
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  /* شعلة الستريك */
  .streak-pill {
    display: flex;
    align-items: center;
    gap: 5px;
    background: var(--orange-soft);
    border: 1px solid rgba(255, 107, 0, 0.2);
    padding: 6px 12px;
    border-radius: var(--radius-pill);
    cursor: pointer;
    font-size: 0.76rem;
    font-weight: 800;
    color: var(--orange-fire);
    transition: transform 0.2s;
  }
  .streak-pill:active { transform: scale(0.95); }
  .streak-pill i {
    animation: flamePulse 1.4s infinite alternate ease-in-out;
  }
  @keyframes flamePulse {
    from { transform: scale(0.9) rotate(-4deg); }
    to { transform: scale(1.2) rotate(4deg); }
  }

  /* مياه الشرب */
  .water-pill {
    display: flex;
    align-items: center;
    gap: 6px;
    background: var(--blue-soft);
    border: 1px solid rgba(2, 132, 199, 0.2);
    padding: 6px 10px;
    border-radius: var(--radius-pill);
    cursor: pointer;
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--blue-sport);
  }

  main {
    max-width: 480px;
    margin: 0 auto;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .clean-card {
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-xl);
    padding: 18px;
    box-shadow: var(--shadow-card);
    position: relative;
    overflow: hidden;
  }

  /* ===== بطاقة الطاقة والداشبورد المركزية ===== */
  .energy-hero {
    background: linear-gradient(175deg, #FFFFFF 0%, #F8FAFC 100%);
    border: 1px solid #E2E8F0;
    box-shadow: var(--shadow-soft);
    padding: 22px 18px;
  }
  .energy-hero-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
  }
  .gauge-box {
    position: relative;
    width: 122px;
    height: 122px;
    flex-shrink: 0;
  }
  .gauge-box svg {
    transform: rotate(-90deg);
    width: 100%;
    height: 100%;
  }
  .gauge-center {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .gauge-center .cals-val {
    font-family: 'Plus Jakarta Sans', 'Almarai', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1;
  }
  .gauge-center .cals-sub {
    font-size: 0.62rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin-top: 4px;
  }

  .hero-intel {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .target-badge {
    background: var(--bg-muted);
    padding: 7px 12px;
    border-radius: var(--radius-md);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.74rem;
    font-weight: 700;
  }

  /* مجسم 3D مصغر تفاعلي في زاوية البطاقة */
  .clay-runner-wrap {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    background: #FFFFFF;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }
  .clay-avatar-3d {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: linear-gradient(135deg, #22C55E 0%, #16A34A 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #FFFFFF;
    font-size: 1rem;
    box-shadow: 0 6px 14px var(--green-lime-glow);
    animation: runnerBounce 1s infinite alternate cubic-bezier(0.4, 0, 0.2, 1);
  }
  @keyframes runnerBounce {
    0% { transform: translateY(0) scale(1); }
    100% { transform: translateY(-4px) scale(1.05); }
  }
  .runner-text {
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--text-primary);
  }
  .runner-sub {
    font-size: 0.58rem;
    color: var(--text-muted);
  }

  /* الماكروز الأفقية النحيفة */
  .macros-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid var(--border-light);
  }
  .macro-card {
    background: #FFFFFF;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 10px 8px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
  }
  .macro-card .m-title {
    font-size: 0.65rem;
    font-weight: 700;
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
    margin-bottom: 2px;
  }
  .macro-card .m-num {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.85rem;
    font-weight: 800;
    color: var(--text-primary);
  }
  .m-progress {
    width: 100%;
    height: 5px;
    background: var(--bg-muted);
    border-radius: 99px;
    margin-top: 6px;
    overflow: hidden;
  }
  .m-progress-bar {
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  }

  /* ===== قسم الوجبات اليومية العائمة (Floating Meals) ===== */
  .section-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 6px;
  }
  .section-head h2 {
    font-size: 0.92rem;
    font-weight: 800;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .reset-indicator {
    font-size: 0.65rem;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 4px;
    background: #FFFFFF;
    padding: 4px 9px;
    border-radius: var(--radius-pill);
    border: 1px solid var(--border-light);
  }

  .floating-meals-grid {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .floating-meal-card {
    background: #FFFFFF;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-lg);
    padding: 14px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: var(--shadow-card);
    transition: transform 0.2s, box-shadow 0.2s;
    position: relative;
    overflow: hidden;
  }
  .floating-meal-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-soft);
  }
  .meal-left {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .food-cutout {
    width: 52px;
    height: 52px;
    border-radius: 16px;
    background: var(--bg-subtle);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    box-shadow: 0 8px 16px -4px rgba(0,0,0,0.06);
    flex-shrink: 0;
  }
  .meal-info h3 {
    font-size: 0.85rem;
    font-weight: 800;
    color: var(--text-primary);
  }
  .meal-info p {
    font-size: 0.68rem;
    color: var(--text-secondary);
    margin-top: 2px;
  }
  .meal-right {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .meal-cals {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.88rem;
    font-weight: 800;
    color: var(--green-lime);
  }
  .quick-add-btn {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: var(--green-soft);
    color: var(--green-lime);
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.85rem;
    transition: all 0.2s;
  }
  .quick-add-btn:active {
    background: var(--green-lime);
    color: #FFFFFF;
    transform: scale(0.92);
  }

  /* ===== كاميرا الذكاء الاصطناعي والباركود ===== */
  .camera-toggle-tabs {
    display: grid;
    grid-template-columns: 1fr 1fr;
    background: var(--bg-muted);
    padding: 4px;
    border-radius: var(--radius-pill);
    gap: 4px;
    margin-bottom: 14px;
  }
  .cam-tab-btn {
    border: none;
    background: transparent;
    padding: 10px;
    border-radius: var(--radius-pill);
    font-size: 0.74rem;
    font-weight: 800;
    color: var(--text-secondary);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    transition: all 0.2s;
  }
  .cam-tab-btn.active {
    background: #FFFFFF;
    color: var(--text-primary);
    box-shadow: 0 4px 10px rgba(0,0,0,0.06);
  }

  /* إطار المسح الليزري */
  .scan-viewfinder {
    position: relative;
    width: 100%;
    height: 240px;
    background: #0F172A;
    border-radius: var(--radius-lg);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #FFFFFF;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.5);
  }
  .scan-viewfinder img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: none;
  }
  .laser-line {
    position: absolute;
    width: 80%;
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--green-lime), transparent);
    box-shadow: 0 0 14px var(--green-lime);
    animation: laserScan 2.2s infinite ease-in-out;
  }
  @keyframes laserScan {
    0% { top: 15%; opacity: 0.3; }
    50% { top: 80%; opacity: 1; }
    100% { top: 15%; opacity: 0.3; }
  }
  .bounding-corner {
    position: absolute;
    width: 24px;
    height: 24px;
    border: 3px solid var(--green-lime);
  }
  .corner-tl { top: 20px; left: 20px; border-right: none; border-bottom: none; border-radius: 8px 0 0 0; }
  .corner-tr { top: 20px; right: 20px; border-left: none; border-bottom: none; border-radius: 0 8px 0 0; }
  .corner-bl { bottom: 20px; left: 20px; border-right: none; border-top: none; border-radius: 0 0 0 8px; }
  .corner-br { bottom: 20px; right: 20px; border-left: none; border-top: none; border-radius: 0 0 8px 0; }

  /* زر التصوير الدائري العصبي */
  .capture-trigger-wrap {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 14px;
    gap: 14px;
  }
  .capture-btn {
    width: 66px;
    height: 66px;
    border-radius: 50%;
    background: #FFFFFF;
    border: 4px solid var(--green-lime);
    box-shadow: 0 6px 20px var(--green-lime-glow);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--green-lime);
    font-size: 1.4rem;
    transition: transform 0.15s;
  }
  .capture-btn:active {
    transform: scale(0.9);
  }

  /* ===== المدرب وكورس التمارين الذكي (القياسات والدهون) ===== */
  .measurements-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 8px;
  }
  .input-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--text-secondary);
    margin-bottom: 4px;
    display: block;
  }
  .clean-input {
    width: 100%;
    padding: 11px 14px;
    background: var(--bg-subtle);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    color: var(--text-primary);
    font-family: inherit;
    font-size: 0.84rem;
    outline: none;
    transition: border-color 0.2s, background 0.2s;
  }
  .clean-input:focus {
    border-color: var(--green-lime);
    background: #FFFFFF;
  }

  /* أزرار الإجراءات الأساسية (CTA) بنظام نيون أخضر */
  .btn-cta {
    width: 100%;
    background: var(--green-lime);
    color: #FFFFFF;
    border: none;
    border-radius: var(--radius-pill);
    padding: 14px;
    font-size: 0.88rem;
    font-weight: 800;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    box-shadow: 0 8px 24px var(--green-lime-glow);
    transition: transform 0.15s, box-shadow 0.2s;
  }
  .btn-cta:active {
    transform: scale(0.98);
  }
  .btn-cta:disabled {
    background: var(--text-muted);
    box-shadow: none;
    cursor: not-allowed;
  }

  /* ===== شريط التنقل السفلي العائم (Floating Dock) ===== */
  .bottom-dock {
    position: fixed;
    bottom: 16px;
    left: 50%;
    transform: translateX(-50%);
    width: calc(100% - 32px);
    max-width: 440px;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(226, 232, 240, 0.8);
    border-radius: 30px;
    padding: 8px 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-floating);
    z-index: 50;
  }
  .dock-btn {
    background: transparent;
    border: none;
    color: var(--text-muted);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3px;
    cursor: pointer;
    font-size: 0.65rem;
    font-weight: 700;
    flex: 1;
    transition: color 0.2s;
  }
  .dock-btn i {
    font-size: 1.15rem;
    transition: transform 0.2s;
  }
  .dock-btn.active {
    color: var(--green-lime);
  }
  .dock-btn.active i {
    transform: translateY(-2px);
  }

  /* زر الإضافة السريع البارز في المنتصف (FAB) */
  .fab-center {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, #22C55E 0%, #16A34A 100%);
    border: 3px solid #FFFFFF;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    cursor: pointer;
    box-shadow: 0 8px 24px var(--green-lime-glow);
    transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    flex-shrink: 0;
    margin-top: -24px;
  }
  .fab-center.open {
    transform: rotate(45deg);
    background: var(--text-primary);
  }

  /* قائمة التفرعات للـ FAB */
  .fab-menu {
    position: fixed;
    bottom: 84px;
    left: 50%;
    transform: translateX(-50%) scale(0.85);
    opacity: 0;
    pointer-events: none;
    display: flex;
    gap: 14px;
    transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    z-index: 49;
  }
  .fab-menu.show {
    opacity: 1;
    pointer-events: auto;
    transform: translateX(-50%) scale(1);
  }
  .fab-item {
    background: #FFFFFF;
    border: 1px solid var(--border-light);
    border-radius: 50%;
    width: 50px;
    height: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: var(--shadow-floating);
    cursor: pointer;
    color: var(--text-primary);
    font-size: 1.1rem;
    transition: transform 0.15s;
  }
  .fab-item:active { transform: scale(0.9); }

  /* ===== النوافذ المنبثقة (Modals & Bottom Sheets) ===== */
  .modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, 0.4);
    backdrop-filter: blur(5px);
    display: none;
    align-items: flex-end;
    justify-content: center;
    z-index: 100;
  }
  .modal-overlay.show {
    display: flex;
  }
  .bottom-sheet {
    background: #FFFFFF;
    border-radius: 28px 28px 0 0;
    width: 100%;
    max-width: 480px;
    max-height: 88vh;
    overflow-y: auto;
    padding: 24px 20px 30px;
    animation: sheetUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 -10px 40px rgba(0,0,0,0.1);
  }
  @keyframes sheetUp {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
  }
  .sheet-handle {
    width: 42px;
    height: 5px;
    background: var(--border);
    border-radius: 99px;
    margin: 0 auto 16px;
  }

  /* بطاقة اشتراك برو المميزة */
  .pro-modal-box {
    background: linear-gradient(180deg, #FFFFFF 0%, #FFFBEB 100%);
    border: 2px solid #FDE68A;
  }
  .golden-3d-statue {
    width: 72px;
    height: 72px;
    margin: 0 auto 10px;
    border-radius: 50%;
    background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #FFFFFF;
    font-size: 2rem;
    box-shadow: 0 10px 30px rgba(245, 158, 11, 0.35);
    animation: goldStatuePulse 2.5s infinite ease-in-out;
  }
  @keyframes goldStatuePulse {
    0%, 100% { transform: scale(1) rotate(0deg); }
    50% { transform: scale(1.08) rotate(4deg); }
  }
  .pricing-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 16px 0;
  }
  .price-card {
    border: 2px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 14px;
    text-align: center;
    background: #FFFFFF;
    cursor: pointer;
    transition: all 0.2s;
  }
  .price-card.selected {
    border-color: var(--orange-fire);
    background: var(--orange-soft);
  }
  .save-tag {
    background: var(--orange-fire);
    color: #FFFFFF;
    font-size: 0.58rem;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: var(--radius-pill);
    display: inline-block;
    margin-bottom: 4px;
  }

  /* Toast Notification */
  #toastContainer {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 120;
    display: flex;
    flex-direction: column;
    gap: 8px;
    width: calc(100% - 32px);
    max-width: 400px;
    pointer-events: none;
  }
  .clean-toast {
    background: #FFFFFF;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 12px 16px;
    font-size: 0.78rem;
    font-weight: 700;
    box-shadow: var(--shadow-floating);
    display: flex;
    align-items: center;
    gap: 10px;
    animation: toastPop 0.25s ease;
  }
  @keyframes toastPop {
    from { transform: translateY(-16px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }

  /* تنبيه بلوغ الحد اليومي */
  .limit-warn-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 12px;
    margin-bottom: 8px;
    background: var(--orange-soft);
    border: 1px solid rgba(255, 107, 0, 0.25);
    border-radius: var(--radius-md);
    font-size: 0.78rem;
    font-weight: 700;
    color: #9A3412;
  }

  .hidden { display: none !important; }
</style>
</head>
<body>

<header>
  <div class="header-inner">
    <div class="user-badge" onclick="openProfileModal()">
      <div class="avatar-wrap">
        <span id="headerAvatarChar">م</span>
        <span class="pro-badge" id="proBadgeTag" onclick="openProModal(event)">PRO</span>
      </div>
      <div class="user-meta">
        <h1 id="headerUserName">مستخدم</h1>
        <p>الهدف: <span id="headerUserGoal">تنشيف وعجز ذكي</span></p>
      </div>
    </div>
    
    <div class="header-actions">
      <!-- شعلة الستريك التفاعلية -->
      <div class="streak-pill" onclick="showStreakInfo()" title="الستريك اليومي">
        <i class="fa-solid fa-fire"></i>
        <span id="streakCount">1 يوم</span>
      </div>
      <!-- ترطيب الماء اليومي -->
      <div class="water-pill" onclick="addWaterCup()">
        <i class="fa-solid fa-droplet"></i>
        <span id="waterCounter">1.5 / 3L</span>
      </div>
    </div>
  </div>
</header>

<main>

  <!-- ================= 1. الشاشة الرئيسية (Home / Dashboard) ================= -->
  <div id="viewHome">
    <!-- بطاقة الطاقة المركزية -->
    <section class="clean-card energy-hero">
      <div class="energy-hero-top">
        <div class="gauge-box">
          <svg viewBox="0 0 120 120">
            <circle cx="60" cy="60" r="50" fill="none" stroke="#E2E8F0" stroke-width="11"/>
            <circle id="calorieGaugeProgress" cx="60" cy="60" r="50" fill="none" stroke="var(--green-lime)" stroke-width="11"
                    stroke-linecap="round" stroke-dasharray="314.15" stroke-dashoffset="314.15" style="transition: stroke-dashoffset 0.8s;"/>
          </svg>
          <div class="gauge-center">
            <span class="cals-val" id="remainingCalsText">1,650</span>
            <span class="cals-sub">سعرة متبقية</span>
          </div>
        </div>

        <div class="hero-intel">
          <div class="target-badge">
            <span style="color:var(--text-secondary);"><i class="fa-solid fa-bullseye" style="color:var(--orange-fire);"></i> الهدف اليومي</span>
            <span style="font-family:'Plus Jakarta Sans';" id="heroTargetCals">2,100 Kcal</span>
          </div>

          <!-- مجسم النشاط التفاعلي 3D -->
          <div class="clay-runner-wrap">
            <div class="clay-avatar-3d">
              <i class="fa-solid fa-person-running"></i>
            </div>
            <div>
              <p class="runner-text" id="runnerEnergyStatus">نشاط منتظم ومستقر</p>
              <p class="runner-sub">تصفير السجل يومياً 7:00 ص</p>
            </div>
          </div>
        </div>
      </div>

      <!-- تفصيل الماكروز بالأشرطة الملونة -->
      <div class="macros-strip">
        <div class="macro-card">
          <p class="m-title"><i class="fa-solid fa-drumstick-bite" style="color:var(--green-lime);"></i> بروتين</p>
          <p class="m-num" id="heroProteinText">45 / 150g</p>
          <div class="m-progress"><div class="m-progress-bar" id="heroProteinBar" style="background:var(--green-lime); width: 30%;"></div></div>
        </div>
        <div class="macro-card">
          <p class="m-title"><i class="fa-solid fa-wheat-awn" style="color:var(--orange-fire);"></i> كارب</p>
          <p class="m-num" id="heroCarbText">80 / 210g</p>
          <div class="m-progress"><div class="m-progress-bar" id="heroCarbBar" style="background:var(--orange-fire); width: 38%;"></div></div>
        </div>
        <div class="macro-card">
          <p class="m-title"><i class="fa-solid fa-droplet" style="color:var(--blue-sport);"></i> دهون</p>
          <p class="m-num" id="heroFatText">20 / 55g</p>
          <div class="m-progress"><div class="m-progress-bar" id="heroFatBar" style="background:var(--blue-sport); width: 36%;"></div></div>
        </div>
      </div>
    </section>

    <!-- قائمة الوجبات العائمة -->
    <div class="section-head">
      <h2><i class="fa-solid fa-plate-wheat" style="color:var(--green-lime);"></i> وجبات اليوم المسجلة</h2>
      <div class="reset-indicator">
        <i class="fa-regular fa-clock"></i> يرست 7:00 ص
      </div>
    </div>

    <div class="floating-meals-grid" id="todayMealsContainer">
      <!-- توليد الوجبات ديناميكياً هنا -->
    </div>
  </div>

  <!-- ================= 2. واجهة كاميرا الذكاء الاصطناعي والباركود ================= -->
  <div id="viewCamera" class="hidden">
    <section class="clean-card">
      <div class="camera-toggle-tabs">
        <button class="cam-tab-btn active" id="btnModeFood" onclick="switchScannerMode('food')">
          <i class="fa-solid fa-wand-magic-sparkles"></i> مسح الصحن بالـ AI
        </button>
        <button class="cam-tab-btn" id="btnModeBarcode" onclick="switchScannerMode('barcode')">
          <i class="fa-solid fa-barcode"></i> فحص الباركود
        </button>
      </div>

      <!-- إطار الكاميرا الليزري -->
      <div class="scan-viewfinder" id="viewfinder">
        <div class="laser-line" id="laserScanLine"></div>
        <div class="bounding-corner corner-tl"></div>
        <div class="bounding-corner corner-tr"></div>
        <div class="bounding-corner corner-bl"></div>
        <div class="bounding-corner corner-br"></div>
        
        <img id="scannedFoodPreview" alt="معاينة الصحن">

        <div id="viewfinderPrompt" style="text-align:center; padding:16px; z-index:2;">
          <i class="fa-solid fa-camera" style="font-size:2.2rem; color:var(--green-lime); margin-bottom:8px;"></i>
          <p id="viewfinderStatusText" style="font-size:0.8rem; font-weight:700;">وجّه الكاميرا نحو طبقك أو الباركود</p>
          <p style="font-size:0.65rem; color:#94A3B8; margin-top:4px;">تتبع ليزري فوري للمكونات والحصص</p>
        </div>
      </div>

      <!-- إدخال يدوي سريع للباركود في حال تعذر تشغيل الكاميرا -->
      <div id="manualBarcodeInputWrap" class="hidden" style="margin-top:12px;">
        <label class="input-label">أو ادخل رقم الباركود مباشرة للبحث:</label>
        <div style="display:flex; gap:8px;">
          <input type="text" id="barcodeNumberInput" class="clean-input" placeholder="مثلاً: 6281007010015">
          <button onclick="searchBarcodeManual()" class="btn-cta" style="width:auto; padding:10px 18px;">
            <i class="fa-solid fa-magnifying-glass"></i>
          </button>
        </div>
      </div>

      <!-- ملاحظة وجبة عند مسح الصحن -->
      <div id="mealNoteWrap" style="margin-top:12px;">
        <label class="input-label">ملاحظة عن المكونات (اختياري للتدقيق الجرامي):</label>
        <input type="text" id="foodContextNote" class="clean-input" placeholder="مثال: صدر دجاج 180 جم + رز عنبر بدون دهن">
      </div>

      <input type="file" id="cameraFileInput" accept="image/*" capture="environment" style="display:none;" onchange="handleFoodImageSelected(event)">
      <input type="file" id="galleryFileInput" accept="image/*" style="display:none;" onchange="handleFoodImageSelected(event)">

      <!-- زر الالتقاط العصبي -->
      <div class="capture-trigger-wrap">
        <button class="quick-add-btn" onclick="document.getElementById('galleryFileInput').click()" style="width:44px; height:44px; font-size:1.1rem;" title="من المعرض">
          <i class="fa-solid fa-images"></i>
        </button>

        <button class="capture-btn" id="btnMainCapture" onclick="triggerScanAction()">
          <i class="fa-solid fa-fingerprint"></i>
        </button>

        <button class="quick-add-btn" onclick="openManualMealModal()" style="width:44px; height:44px; font-size:1.1rem;" title="إدخال يدوي">
          <i class="fa-solid fa-pen-to-square"></i>
        </button>
      </div>

      <!-- نتيجة فحص الذكاء الاصطناعي للصحن -->
      <div id="aiFoodResultCard" class="clean-card hidden" style="margin-top:14px; background:var(--bg-subtle);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <h3 id="resFoodName" style="font-size:0.9rem; font-weight:800; color:var(--green-lime);">اسم الصحن</h3>
          <span id="resFoodCals" style="font-weight:900; color:var(--text-primary); font-size:0.95rem;">0 سعرة</span>
        </div>
        <p id="resFoodDesc" style="font-size:0.72rem; color:var(--text-secondary); line-height:1.6; margin-bottom:10px;"></p>
        
        <div class="macros-strip" style="margin-top:8px; padding-top:8px;">
          <div class="macro-card"><span class="m-title">بروتين</span><span id="resFoodP" class="m-num">0g</span></div>
          <div class="macro-card"><span class="m-title">كارب</span><span id="resFoodC" class="m-num">0g</span></div>
          <div class="macro-card"><span class="m-title">دهون</span><span id="resFoodF" class="m-num">0g</span></div>
        </div>

        <button onclick="confirmAddScannedMeal()" class="btn-cta" style="margin-top:12px;">
          <i class="fa-solid fa-plus"></i> إضافة الصحن إلى سجل اليوم
        </button>
      </div>
    </section>
  </div>

  <!-- ================= 3. قسم التمارين وكورس الجسم الذكي ================= -->
  <div id="viewWorkouts" class="hidden">
    <section class="clean-card">
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
        <div class="clay-avatar-3d" style="background:var(--blue-sport); box-shadow:0 6px 14px rgba(2, 132, 199, 0.3);">
          <i class="fa-solid fa-dumbbell"></i>
        </div>
        <div>
          <h2 style="font-size:0.95rem; font-weight:800;">كورس الجسم والتمارين المفصل</h2>
          <p style="font-size:0.68rem; color:var(--text-secondary);">حسب قياسات الخصر، الفخذ ومناطق تركز الدهون</p>
        </div>
      </div>

      <div class="measurements-grid">
        <div>
          <label class="input-label">محيط الخصر (سم):</label>
          <input type="number" id="inputWaist" class="clean-input" value="84" placeholder="مثلاً: 84">
        </div>
        <div>
          <label class="input-label">محيط الفخذ (سم):</label>
          <input type="number" id="inputThigh" class="clean-input" value="56" placeholder="مثلاً: 56">
        </div>
      </div>

      <div style="margin-top:10px;">
        <label class="input-label">مناطق تركز الدهون الملحوظة:</label>
        <select id="selectFatZones" class="clean-input">
          <option value="أسفل البطن والخواصر (Love handles)">أسفل البطن والخواصر</option>
          <option value="الصدر ومنطقة الأكتاف">الصدر والأكتاف</option>
          <option value="الأرداف والفخذين السفليين">الأرداف والأفخاذ</option>
          <option value="توزيع دهون متجانس في كل الجسم">دهون موزعة بالتساوي</option>
        </select>
      </div>

      <div style="margin-top:10px;">
        <label class="input-label">مكان ومعدات التمرين:</label>
        <select id="selectWorkoutEnv" class="clean-input">
          <option value="في الجيم بأجهزة وأوزان حرة متكاملة">في الجيم (أوزان وأجهزة كاملة)</option>
          <option value="في البيت بوزن الجسم فقط (Calisthenics)">في البيت (وزن الجسم فقط)</option>
          <option value="في البيت مع زوج دمبلز وحبل مقاومة">في البيت (دمبلز ومقاومة)</option>
        </select>
      </div>

      <button onclick="generateCustomWorkoutAI()" id="btnGenerateWorkout" class="btn-cta" style="margin-top:14px;">
        <i class="fa-solid fa-bolt"></i> توليد جدول التمارين والتكنيك الذكي
      </button>

      <div id="workoutResultBox" class="clean-card hidden" style="margin-top:14px; background:var(--bg-subtle); line-height:1.7; font-size:0.75rem; white-space:pre-line;">
        <!-- جدول التمارين الذكي -->
      </div>
    </section>

    <!-- كورس غذائي حسب الطعام المتوفر -->
    <section class="clean-card" style="margin-top:14px;">
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <div class="clay-avatar-3d" style="background:var(--orange-fire); box-shadow:0 6px 14px var(--orange-glow);">
          <i class="fa-solid fa-kitchen-set"></i>
        </div>
        <div>
          <h2 style="font-size:0.95rem; font-weight:800;">كورس غذائي حسب المتوفر بالبيت</h2>
          <p style="font-size:0.68rem; color:var(--text-secondary);">استغل أكلك وميزانيتك الحالية بذكاء</p>
        </div>
      </div>

      <label class="input-label">الأطعمة والمكونات الموجودة في مطبخك الآن:</label>
      <textarea id="inputPantryFoods" class="clean-input" rows="2" placeholder="مثال: بيض، صدر دجاج، رز، شوفان، خيار، لبن..."></textarea>

      <div class="measurements-grid" style="margin-top:8px;">
        <div>
          <label class="input-label">الميزانية المقترحة:</label>
          <select id="selectPantryBudget" class="clean-input">
            <option value="اقتصادية وبسيطة">اقتصادية ومحدودة</option>
            <option value="متوسطة">متوسطة</option>
            <option value="مفتوحة">مفتوحة</option>
          </select>
        </div>
        <div>
          <label class="input-label">عدد الوجبات المرغوبة:</label>
          <select id="selectMealCount" class="clean-input">
            <option value="3 وجبات رئيسية + سناك">3 وجبات + سناك</option>
            <option value="وجبتين رئيسيتين (صيام متقطع)">وجبتين (صيام متقطع)</option>
            <option value="4 إلى 5 وجبات صغيرة">4 إلى 5 وجبات</option>
          </select>
        </div>
      </div>

      <button onclick="generateCustomDietAI()" id="btnGenerateDiet" class="btn-cta" style="margin-top:14px; background:var(--orange-fire); box-shadow:0 8px 24px var(--orange-glow);">
        <i class="fa-solid fa-utensils"></i> توليد خطة الوجبات الغذائية
      </button>

      <div id="dietResultBox" class="clean-card hidden" style="margin-top:14px; background:var(--bg-subtle); line-height:1.7; font-size:0.75rem; white-space:pre-line;">
        <!-- الخطة الغذائية المقترحة -->
      </div>
    </section>
  </div>

  <!-- ================= 4. قسم التحديات والستريك ================= -->
  <div id="viewAnalytics" class="hidden">
    <section class="clean-card">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <div>
          <h2 style="font-size:0.95rem; font-weight:800;">تحديات الستريك اليومية</h2>
          <p style="font-size:0.68rem; color:var(--text-secondary);">حافظ على الشعلة مشتعلة قبل الساعة 7:00 صباحاً</p>
        </div>
        <div class="streak-pill">
          <i class="fa-solid fa-fire"></i>
          <span id="streakDaysView">1 يوم ستريك</span>
        </div>
      </div>

      <div id="challengesListWrap" style="display:flex; flex-direction:column; gap:10px;">
        <!-- التحديات الأربعة -->
      </div>
    </section>
  </div>

  <!-- ================= 5. قسم الترقية والبروفايل ================= -->
  <div id="viewProfile" class="hidden">
    <section class="clean-card">
      <div style="text-align:center; padding:10px 0;">
        <div class="avatar-wrap" style="width:68px; height:68px; margin:0 auto 10px; font-size:1.6rem;">
          <span id="profileAvatarBig">م</span>
        </div>
        <h2 id="profileBigName" style="font-size:1.1rem; font-weight:800;">مستخدم</h2>
        <span class="pro-badge" id="profileProBadge" style="position:static; display:inline-block; margin-top:4px; font-size:0.7rem; padding:3px 10px;">عضوية PRO الذهبية</span>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:16px;">
        <div class="macro-card">
          <span class="m-title">الوزن الحالي</span>
          <span id="profStatWeight" class="m-num">75 كغم</span>
        </div>
        <div class="macro-card">
          <span class="m-title">الطول</span>
          <span id="profStatHeight" class="m-num">175 سم</span>
        </div>
      </div>

      <div style="margin-top:16px; display:flex; flex-direction:column; gap:8px;">
        <button onclick="openProfileModal()" class="btn-cta" style="background:#FFFFFF; color:var(--text-primary); border:1px solid var(--border); box-shadow:none;">
          <i class="fa-solid fa-user-pen"></i> تعديل بيانات الجسم والهدف
        </button>
        <button onclick="openProModal()" class="btn-cta" style="background:linear-gradient(135deg, #F59E0B, #D97706); box-shadow:0 8px 24px rgba(245, 158, 11, 0.3);">
          <i class="fa-solid fa-crown"></i> تفعيل كود الاشتراك أو التجديد
        </button>
        <a href="https://wa.me/9647822332083" target="_blank" class="btn-cta" style="text-decoration:none; background:#25D366; box-shadow:0 6px 18px rgba(37, 211, 102, 0.25);">
          <i class="fa-brands fa-whatsapp" style="font-size:1.1rem;"></i> تواصل مع المطور عبر واتساب (07822332083)
        </a>
      </div>

      <!-- ذيل الصفحة: أسماء المطورين -->
      <div style="margin-top:24px; padding-top:16px; border-top:1px solid var(--border-light); text-align:center;">
        <p style="font-size:0.65rem; color:var(--text-muted); font-weight:700; margin-bottom:4px;">
          فريق التطوير والبرمجة (Developers)
        </p>
        <p style="font-family:'Plus Jakarta Sans', sans-serif; font-size:0.75rem; font-weight:800; color:var(--text-primary); direction:ltr; letter-spacing:0.3px;">
          mohtade haider ali / mahde mueen / jafar alsadeq
        </p>
      </div>
    </section>
  </div>

</main>

<!-- ================= شريط التنقل السفلي العائم (Floating Dock) ================= -->
<nav class="bottom-dock">
  <button class="dock-btn active" id="dockBtnHome" onclick="switchMainTab('home')">
    <i class="fa-solid fa-house"></i>
    <span>الرئيسية</span>
  </button>

  <button class="dock-btn" id="dockBtnWorkouts" onclick="switchMainTab('workouts')">
    <i class="fa-solid fa-dumbbell"></i>
    <span>التمارين</span>
  </button>

  <!-- زر الإضافة المركزي العائم FAB -->
  <button class="fab-center" id="mainFabBtn" onclick="toggleFabMenu()">
    <i class="fa-solid fa-plus"></i>
  </button>

  <button class="dock-btn" id="dockBtnAnalytics" onclick="switchMainTab('analytics')">
    <i class="fa-solid fa-chart-simple"></i>
    <span>التحديات</span>
  </button>

  <button class="dock-btn" id="dockBtnProfile" onclick="switchMainTab('profile')">
    <i class="fa-solid fa-user"></i>
    <span>حسابي</span>
  </button>
</nav>

<!-- القائمة المتفرعة من الـ FAB -->
<div class="fab-menu" id="fabMenu">
  <div class="fab-item" onclick="openCameraView('food')" title="مسح الصحن AI">
    <i class="fa-solid fa-wand-magic-sparkles" style="color:var(--green-lime);"></i>
  </div>
  <div class="fab-item" onclick="openCameraView('barcode')" title="فحص الباركود">
    <i class="fa-solid fa-barcode" style="color:var(--blue-sport);"></i>
  </div>
  <div class="fab-item" onclick="openManualMealModal()" title="إضافة وجبة يدوياً">
    <i class="fa-solid fa-pen" style="color:var(--orange-fire);"></i>
  </div>
</div>

<!-- ================= نافذة منبثقة: نتيجة الباركود ================= -->
<div class="modal-overlay" id="barcodeResultModal">
  <div class="bottom-sheet">
    <div class="sheet-handle"></div>
    <div style="text-align:center; margin-bottom:14px;">
      <div class="food-cutout" style="width:64px; height:64px; margin:0 auto 10px; font-size:1.8rem;" id="barcodeProductImgWrap">
        🥫
      </div>
      <h3 id="barcodeProdName" style="font-size:1.05rem; font-weight:800;">اسم المنتج المعلب</h3>
      <p id="barcodeProdServing" style="font-size:0.7rem; color:var(--text-secondary);">حجم الحصة: 100 جم</p>
    </div>

    <div class="macros-strip" style="margin-top:0; border:none;">
      <div class="macro-card"><span class="m-title">السعرات</span><span id="barcodeProdCals" class="m-num">0</span></div>
      <div class="macro-card"><span class="m-title">بروتين</span><span id="barcodeProdP" class="m-num">0g</span></div>
      <div class="macro-card"><span class="m-title">كارب</span><span id="barcodeProdC" class="m-num">0g</span></div>
    </div>

    <!-- التحذيرات الغذائية الذكية -->
    <div id="barcodeWarningsWrap" style="margin:14px 0; display:flex; flex-direction:column; gap:6px;">
      <!-- تحذيرات السكر والدهون المضافة -->
    </div>

    <button onclick="addBarcodeMealToLog()" class="btn-cta">
      <i class="fa-solid fa-plus"></i> إضافة المنتج إلى وجبات اليوم
    </button>
    <button onclick="closeModal('barcodeResultModal')" class="btn-cta" style="background:transparent; color:var(--text-secondary); box-shadow:none; margin-top:6px;">
      إغلاق
    </button>
  </div>
</div>

<!-- ================= نافذة منبثقة: الباركود غير مسجل ================= -->
<div class="modal-overlay" id="barcodeNotFoundModal">
  <div class="bottom-sheet" style="text-align:center;">
    <div class="sheet-handle"></div>
    <div style="width:60px; height:60px; border-radius:50%; background:#FEE2E2; color:#EF4444; display:flex; align-items:center; justify-content:center; font-size:1.8rem; margin:0 auto 12px;">
      <i class="fa-solid fa-circle-question"></i>
    </div>
    <h3 style="font-size:1rem; font-weight:800; margin-bottom:6px;">عذراً، المنتج غير مسجل</h3>
    <p style="font-size:0.75rem; color:var(--text-secondary); line-height:1.6; margin-bottom:16px;">
      لم نتمكن من العثور على هذا الباركود في قاعدة بيانات المنتجات المعلبة. يمكنك كتابة معلوماته وإضافته يدوياً بثوانٍ!
    </p>
    
    <button onclick="openManualMealFromNotFound()" class="btn-cta">
      <i class="fa-solid fa-pen-to-square"></i> إضافة القيم الغذائية يدوياً
    </button>
    <button onclick="closeModal('barcodeNotFoundModal')" class="btn-cta" style="background:transparent; color:var(--text-secondary); box-shadow:none; margin-top:6px;">
      إلغاء
    </button>
  </div>
</div>

<!-- ================= نافذة منبثقة: إضافة وجبة يدوياً ================= -->
<div class="modal-overlay" id="manualMealModal">
  <div class="bottom-sheet">
    <div class="sheet-handle"></div>
    <h3 style="font-size:1rem; font-weight:800; margin-bottom:12px;"><i class="fa-solid fa-pen-to-square" style="color:var(--green-lime);"></i> إضافة وجبة مخصصة</h3>
    
    <label class="input-label">اسم الوجبة / المنتج:</label>
    <input type="text" id="manualMealName" class="clean-input" placeholder="مثلاً: علبة تونة أو 2 بيض مسلوق">

    <div class="measurements-grid" style="margin-top:8px;">
      <div>
        <label class="input-label">السعرات (Kcal):</label>
        <input type="number" id="manualMealCals" class="clean-input" placeholder="مثلاً: 250">
      </div>
      <div>
        <label class="input-label">البروتين (جم):</label>
        <input type="number" id="manualMealProtein" class="clean-input" placeholder="مثلاً: 30">
      </div>
    </div>

    <div class="measurements-grid" style="margin-top:8px;">
      <div>
        <label class="input-label">الكاربوهيدرات (جم):</label>
        <input type="number" id="manualMealCarb" class="clean-input" placeholder="مثلاً: 10">
      </div>
      <div>
        <label class="input-label">الدهون (جم):</label>
        <input type="number" id="manualMealFat" class="clean-input" placeholder="مثلاً: 5">
      </div>
    </div>

    <button onclick="submitManualMeal()" class="btn-cta" style="margin-top:16px;">
      <i class="fa-solid fa-check"></i> حفظ الوجبة في السجل
    </button>
    <button onclick="closeModal('manualMealModal')" class="btn-cta" style="background:transparent; color:var(--text-secondary); box-shadow:none; margin-top:4px;">
      إلغاء
    </button>
  </div>
</div>

<!-- ================= نافذة منبثقة: اشتراك PRO والأكواد ================= -->
<div class="modal-overlay" id="proSubscriptionModal">
  <div class="bottom-sheet pro-modal-box">
    <div class="sheet-handle"></div>
    <div class="golden-3d-statue">
      <i class="fa-solid fa-shield-halved"></i>
    </div>
    
    <h3 style="text-align:center; font-size:1.15rem; font-weight:900;">ترقية فيت سمارت PRO</h3>
    <p style="text-align:center; font-size:0.74rem; color:var(--text-secondary); margin-top:3px;">
      ذكاء اصطناعي فائق، مسح باركود بلا حدود، وخطط كمال أجسام وتغذية متكاملة
    </p>

    <!-- خيارات الاشتراك: شهري 7 آلاف / سنوي 70 ألف -->
    <div class="pricing-cards">
      <div class="price-card selected" id="optMonthly" onclick="selectSubOption('monthly')">
        <p style="font-size:0.8rem; font-weight:800;">شهري</p>
        <p style="font-size:1.1rem; font-weight:900; color:var(--text-primary); margin:4px 0;">7,000 <span style="font-size:0.65rem;">د.ع</span></p>
        <span style="font-size:0.62rem; color:var(--text-muted);">تجديد كل 30 يوم</span>
      </div>

      <div class="price-card" id="optYearly" onclick="selectSubOption('yearly')">
        <span class="save-tag">توفير 40%</span>
        <p style="font-size:0.8rem; font-weight:800;">سنوي</p>
        <p style="font-size:1.1rem; font-weight:900; color:var(--orange-fire); margin:4px 0;">70,000 <span style="font-size:0.65rem;">د.ع</span></p>
        <span style="font-size:0.62rem; color:var(--text-muted);">عام كامل بلا قيود</span>
      </div>
    </div>

    <!-- إدخال كود التفعيل المكون من 4 رموز -->
    <div style="background:#FFFFFF; border:1px solid #FDE68A; border-radius:var(--radius-lg); padding:14px; margin-bottom:14px;">
      <label class="input-label" style="color:var(--text-primary);"><i class="fa-solid fa-key" style="color:var(--gold-pro);"></i> كود التفعيل الخاص بك (4 رموز):</label>
      <div style="display:flex; gap:8px;">
        <input type="text" id="activationCodeInput" class="clean-input" maxlength="6" placeholder="مثلاً: AB82" style="text-align:center; letter-spacing:3px; font-weight:900; font-size:1rem; text-transform:uppercase;">
        <button onclick="redeemActivationCode()" class="btn-cta" style="width:auto; padding:10px 20px; background:linear-gradient(135deg, #F59E0B, #D97706); box-shadow:none;">
          تفعيل
        </button>
      </div>
    </div>

    <!-- زر التجربة المجانية لمدة 7 أيام -->
    <button onclick="startFreeTrial()" class="btn-cta" style="margin-bottom:10px; background:linear-gradient(135deg, #22C55E 0%, #16A34A 100%);">
      <i class="fa-solid fa-gift"></i> ابدأ التجربة المجانية لمدة 7 أيام
    </button>

    <!-- زر التواصل مع المطور عبر واتساب لشراء الأكواد -->
    <a href="https://wa.me/9647822332083" target="_blank" class="btn-cta" style="text-decoration:none; margin-bottom:10px; background:#25D366; box-shadow:0 8px 24px rgba(37, 211, 102, 0.28);">
      <i class="fa-brands fa-whatsapp" style="font-size:1.1rem;"></i> تواصل مع المطور على واتساب (07822332083)
    </a>

    <button onclick="closeModal('proSubscriptionModal')" class="btn-cta" style="background:transparent; color:var(--text-secondary); box-shadow:none;">
      إغلاق
    </button>
  </div>
</div>

<!-- ================= نافذة منبثقة: إدخال وتعديل بيانات الجسم ================= -->
<div class="modal-overlay" id="profileModal">
  <div class="bottom-sheet">
    <div class="sheet-handle"></div>
    <h3 style="font-size:1rem; font-weight:800; margin-bottom:12px;">بيانات الجسم والهدف الرياضي</h3>
    
    <label class="input-label">الاسم الكامل:</label>
    <input type="text" id="editUserName" class="clean-input" value="" placeholder="اكتب اسمك">

    <div class="measurements-grid" style="margin-top:8px;">
      <div>
        <label class="input-label">الوزن (كغم):</label>
        <input type="number" id="editUserWeight" class="clean-input" value="75">
      </div>
      <div>
        <label class="input-label">الطول (سم):</label>
        <input type="number" id="editUserHeight" class="clean-input" value="175">
      </div>
    </div>

    <div class="measurements-grid" style="margin-top:8px;">
      <div>
        <label class="input-label">العمر:</label>
        <input type="number" id="editUserAge" class="clean-input" value="23">
      </div>
      <div>
        <label class="input-label">الجنس:</label>
        <select id="editUserGender" class="clean-input">
          <option value="male">ذكر</option>
          <option value="female">أنثى</option>
        </select>
      </div>
    </div>

    <div style="margin-top:8px;">
      <label class="input-label">الهدف الحالي:</label>
      <select id="editUserGoal" class="clean-input">
        <option value="lose">خسارة دهون وتنشيف (عجز 500 سعرة)</option>
        <option value="gain">بناء عضلات وتضخيم (فائض 400 سعرة)</option>
        <option value="maintain">ثبات الوزن والمحافظة</option>
      </select>
    </div>

    <button onclick="saveProfileChanges()" class="btn-cta" style="margin-top:16px;">
      <i class="fa-solid fa-check"></i> حفظ وحساب الاحتياج
    </button>
    <button onclick="closeModal('profileModal')" class="btn-cta" style="background:transparent; color:var(--text-secondary); box-shadow:none; margin-top:4px;">
      إلغاء
    </button>
  </div>
</div>

<!-- ================= نافذة التسجيل الأولي (أول فتح للتطبيق) ================= -->
<div class="modal-overlay" id="onboardingModal" style="align-items:center; z-index:110;">
  <div class="bottom-sheet" style="border-radius:28px; max-width:440px; margin:0 16px; max-height:92vh;">
    <div style="text-align:center; margin-bottom:12px;">
      <div class="clay-avatar-3d" style="width:56px; height:56px; font-size:1.5rem; margin:0 auto 8px;">
        <i class="fa-solid fa-heart-pulse"></i>
      </div>
      <h3 style="font-size:1.05rem; font-weight:900;">أهلاً بك في فيت سمارت</h3>
      <p style="font-size:0.72rem; color:var(--text-secondary); margin-top:3px;">سجّل بياناتك مرة واحدة لنحسب احتياجك اليومي بدقة</p>
    </div>

    <label class="input-label">الاسم:</label>
    <input type="text" id="obName" class="clean-input" placeholder="اكتب اسمك" maxlength="30">

    <div class="measurements-grid">
      <div>
        <label class="input-label">الوزن (كغم):</label>
        <input type="number" id="obWeight" class="clean-input" placeholder="مثلاً: 75" inputmode="decimal">
      </div>
      <div>
        <label class="input-label">الطول (سم):</label>
        <input type="number" id="obHeight" class="clean-input" placeholder="مثلاً: 175" inputmode="decimal">
      </div>
    </div>

    <div class="measurements-grid">
      <div>
        <label class="input-label">العمر:</label>
        <input type="number" id="obAge" class="clean-input" placeholder="مثلاً: 25" inputmode="numeric">
      </div>
      <div>
        <label class="input-label">الجنس:</label>
        <select id="obGender" class="clean-input">
          <option value="male">ذكر</option>
          <option value="female">أنثى</option>
        </select>
      </div>
    </div>

    <div style="margin-top:8px;">
      <label class="input-label">هدفك:</label>
      <select id="obGoal" class="clean-input">
        <option value="lose">خسارة دهون وتنشيف (عجز 500 سعرة)</option>
        <option value="gain">بناء عضلات وتضخيم (فائض 400 سعرة)</option>
        <option value="maintain">ثبات الوزن والمحافظة</option>
      </select>
    </div>

    <button onclick="completeOnboarding()" class="btn-cta" style="margin-top:16px;">
      <i class="fa-solid fa-check"></i> ابدأ الآن
    </button>
  </div>
</div>

<!-- ================= نافذة تحذير: بلوغ الحد اليومي من السعرات أو الماكروز ================= -->
<div class="modal-overlay" id="limitWarningModal" style="align-items:center; z-index:105;">
  <div class="bottom-sheet" style="border-radius:28px; max-width:420px; margin:0 16px; text-align:center;">
    <div style="width:60px; height:60px; border-radius:50%; background:var(--orange-soft); color:var(--orange-fire); display:flex; align-items:center; justify-content:center; font-size:1.8rem; margin:0 auto 10px;">
      <i class="fa-solid fa-triangle-exclamation"></i>
    </div>
    <h3 style="font-size:1rem; font-weight:900; margin-bottom:10px;">تنبيه: وصلت للحد اليومي</h3>
    <div id="limitWarningList" style="text-align:right;"></div>
    <button onclick="closeLimitWarning()" class="btn-cta" style="margin-top:8px; background:var(--orange-fire); box-shadow:0 8px 24px var(--orange-glow);">
      فهمت
    </button>
  </div>
</div>

<div id="toastContainer"></div>

<script>
  /* ================= حالة التطبيق والبيانات ================= */
  let userProfile = {
    name: "",
    gender: "male",
    age: 23,
    weight: 75,
    height: 175,
    waist: 84,
    thigh: 56,
    goal: "lose",
    targetCals: 2100,
    targetProtein: 150,
    targetCarb: 210,
    targetFat: 55,
    isPro: false,
    proExpires: null
  };

  let todayMeals = [];
  let waterLiters = 0;
  let streakData = { count: 0, lastCompletedDate: null };
  let currentScanMode = 'food'; // 'food' or 'barcode'
  let capturedBase64Image = null;
  let capturedMime = 'image/jpeg';
  let currentAnalyzedFood = null;
  let currentBarcodeProduct = null;

  /* ================= نظام اشتراك PRO (الخادم هو المرجع) ================= */
  const PRO_STORE_KEY = 'fitsmart_pro';

  function getDeviceId() {
    let id = localStorage.getItem('fitsmart_device_id');
    if (!id) {
      id = (window.crypto && crypto.randomUUID)
        ? crypto.randomUUID()
        : (Date.now().toString(36) + Math.random().toString(36).slice(2) + Math.random().toString(36).slice(2));
      localStorage.setItem('fitsmart_device_id', id);
    }
    return id;
  }

  function getProState() {
    try { return JSON.parse(localStorage.getItem(PRO_STORE_KEY)) || {}; } catch(e) { return {}; }
  }
  function setProState(st) {
    if (st) localStorage.setItem(PRO_STORE_KEY, JSON.stringify(st));
    else localStorage.removeItem(PRO_STORE_KEY);
  }

  function proHeaders(extra) {
    const hd = Object.assign({ 'Content-Type': 'application/json', 'X-Device-Id': getDeviceId() }, extra || {});
    const st = getProState();
    if (st.token) hd['X-Pro-Token'] = st.token;
    return hd;
  }

  let proExpiryTimer = null;
  function applyProState(active, expiresMs) {
    userProfile.isPro = !!active;
    userProfile.proExpires = (active && expiresMs) ? new Date(expiresMs).toISOString() : null;
    renderProStatus();

    // جدولة إلغاء الميزات تلقائياً لحظة انتهاء الاشتراك
    clearTimeout(proExpiryTimer);
    if (active && expiresMs) {
      const ms = expiresMs - Date.now();
      if (ms > 0 && ms < 2147000000) {
        proExpiryTimer = setTimeout(() => { enforceProExpiry(); refreshProStatus(); }, ms + 500);
      }
    }
  }

  // إلغاء ميزات PRO فوراً إذا انتهت المدة المحفوظة
  function enforceProExpiry() {
    const st = getProState();
    if (st.expiresMs && Date.now() >= st.expiresMs) {
      const wasPro = userProfile.isPro;
      setProState(null);
      applyProState(false);
      if (wasPro) showToast("انتهى اشتراك PRO الخاص بك. جدّد الاشتراك لمتابعة استخدام الميزات.", "error");
      return true;
    }
    return false;
  }

  function renderProStatus() {
    const badge = document.getElementById('proBadgeTag');
    const pbadge = document.getElementById('profileProBadge');
    const active = !!userProfile.isPro;
    if (badge) {
      badge.style.filter = active ? '' : 'grayscale(1)';
      badge.style.opacity = active ? '' : '0.7';
    }
    if (pbadge) {
      if (active && userProfile.proExpires) {
        const days = Math.max(1, Math.ceil((new Date(userProfile.proExpires) - Date.now()) / 86400000));
        pbadge.innerText = `عضوية PRO الذهبية — متبقي ${days} يوم`;
      } else {
        pbadge.innerText = `حساب مجاني — المتبقي اليوم ${getAIRemaining()} من ${AI_DAILY_LIMIT} استخدامات للذكاء الاصطناعي`;
      }
    }
  }

  async function refreshProStatus() {
    const st = getProState();
    if (!st.token) { applyProState(false); return; }
    try {
      const res = await fetch('/api/subscription/status', { headers: proHeaders() });
      const data = await res.json();
      if (data.active) {
        st.expiresMs = data.expires_at_ms;
        setProState(st);
        applyProState(true, data.expires_at_ms);
      } else {
        setProState(null);
        applyProState(false);
        if (data.expired) showToast("انتهى اشتراك PRO الخاص بك. جدّد الاشتراك لمتابعة استخدام الميزات.", "error");
      }
    } catch(e) {
      // الخادم غير متاح مؤقتاً: نعتمد على تاريخ الانتهاء المحفوظ
      if (!enforceProExpiry()) applyProState(!!(st.expiresMs && st.expiresMs > Date.now()), st.expiresMs);
    }
  }

  // فحص انتهاء الاشتراك أثناء استخدام التطبيق (كل 30 ثانية)
  setInterval(() => {
    if (enforceProExpiry()) refreshProStatus();
    checkAndExecute7AMReset();
  }, 30000);

  // عند رجوع المستخدم للتطبيق بعد فترة: نتأكد من الاشتراك ومن التصفير اليومي
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) {
      enforceProExpiry();
      refreshProStatus();
      checkAndExecute7AMReset();
    }
  });

  function requirePro() {
    enforceProExpiry();
    if (userProfile.isPro) return true;
    showToast("هذه الميزة متاحة لمشتركي PRO فقط. فعّل كوداً أو ابدأ التجربة المجانية.", "error");
    openModal('proSubscriptionModal');
    return false;
  }

  // fetch للميزات المحمية: يرسل التوكن ويتعامل مع رفض الخادم (402)
  async function proFetch(url, options) {
    const opts = Object.assign({}, options);
    opts.headers = proHeaders(opts.headers);
    const res = await fetch(url, opts);
    if (res.status === 402) {
      let data = {};
      try { data = await res.clone().json(); } catch(e) {}
      setProState(null);
      applyProState(false);
      openModal('proSubscriptionModal');
      showToast(data.error || "هذه الميزة متاحة لمشتركي PRO فقط.", "error");
      const err = new Error(data.error || 'PRO required');
      err.handled = true;
      throw err;
    }
    return res;
  }

  /* ================= التصفير اليومي المؤتمت (الساعة 7:00 صباحاً) ================= */
  function get7AMCycleDate(dateObj) {
    const d = new Date(dateObj);
    if (d.getHours() < 7) {
      d.setDate(d.getDate() - 1);
    }
    return `${d.getFullYear()}-${d.getMonth() + 1}-${d.getDate()}`;
  }

  function checkAndExecute7AMReset() {
    const now = new Date();
    const currentCycle = get7AMCycleDate(now);
    const lastSavedCycle = localStorage.getItem('fitsmart_last_cycle');

    if (lastSavedCycle && lastSavedCycle !== currentCycle) {
      // ريست السجل اليومي للوجبات والماء في السابعة صباحاً
      todayMeals = [];
      waterLiters = 0;
      saveTodayMeals();
      localStorage.setItem('fitsmart_water', 0);
      localStorage.removeItem('fitsmart_challenges');
      try { renderChallenges(); } catch(e) {}
      showToast("🌅 الساعة 7:00 ص: تم تصفير سجل اليوم بنجاح لبدء يوم نشط جديد!", "info");
    }
    localStorage.setItem('fitsmart_last_cycle', currentCycle);
  }

  /* ================= التحميل والتخزين المحلي ================= */
  function loadInitialData() {
    try {
      const savedProf = localStorage.getItem('fitsmart_profile');
      if (savedProf) Object.assign(userProfile, JSON.parse(savedProf));
      userProfile.isPro = false; // لا نثق بالمحفوظ محلياً، الخادم يؤكد الحالة
      userProfile.proExpires = null;

      const savedMeals = localStorage.getItem('fitsmart_meals');
      if (savedMeals) todayMeals = JSON.parse(savedMeals);

      const savedStreak = localStorage.getItem('fitsmart_streak');
      if (savedStreak) Object.assign(streakData, JSON.parse(savedStreak));

      const savedWater = localStorage.getItem('fitsmart_water');
      if (savedWater) waterLiters = parseFloat(savedWater) || 0;
    } catch(e) {}

    // المستخدمون القدامى الذين غيّروا اسمهم سابقاً لا يحتاجون التسجيل من جديد
    let needsOnboarding = localStorage.getItem('fitsmart_onboarded') !== '1';
    if (needsOnboarding && userProfile.name && userProfile.name !== 'مهتدي' && localStorage.getItem('fitsmart_profile')) {
      localStorage.setItem('fitsmart_onboarded', '1');
      needsOnboarding = false;
    }

    checkAndExecute7AMReset();
    checkStreakContinuity();
    recalculateTargets();
    updateUI();
    renderMealsList();
    renderChallenges();
    refreshProStatus();
    initAds();

    if (needsOnboarding) openModal('onboardingModal');
  }

  function saveProfile() {
    const { isPro, proExpires, ...profileToSave } = userProfile;
    localStorage.setItem('fitsmart_profile', JSON.stringify(profileToSave));
    updateUI();
  }

  function saveTodayMeals() {
    localStorage.setItem('fitsmart_meals', JSON.stringify(todayMeals));
    updateUI();
    renderMealsList();
  }

  function saveStreak() {
    localStorage.setItem('fitsmart_streak', JSON.stringify(streakData));
    document.getElementById('streakCount').innerText = `${streakData.count} يوم`;
    document.getElementById('streakDaysView').innerText = `${streakData.count} يوم ستريك`;
  }

  /* ================= حساب السعرات والماكروز ================= */
  function recalculateTargets() {
    const w = parseFloat(userProfile.weight) || 75;
    const h = parseFloat(userProfile.height) || 175;
    const a = parseFloat(userProfile.age) || 23;
    
    let bmr = (10 * w) + (6.25 * h) - (5 * a);
    bmr = userProfile.gender === 'male' ? bmr + 5 : bmr - 161;
    let tdee = bmr * 1.45; // متوسط النشاط

    if (userProfile.goal === 'lose') userProfile.targetCals = Math.round(tdee - 500);
    else if (userProfile.goal === 'gain') userProfile.targetCals = Math.round(tdee + 400);
    else userProfile.targetCals = Math.round(tdee);

    userProfile.targetProtein = Math.round(w * 2.0);
    const protCals = userProfile.targetProtein * 4;
    const fatCals = userProfile.targetCals * 0.25;
    userProfile.targetFat = Math.round(fatCals / 9);
    userProfile.targetCarb = Math.max(50, Math.round((userProfile.targetCals - (protCals + fatCals)) / 4));

    saveProfile();
  }

  /* ================= تحديث واجهة المستخدم (UI) ================= */
  function updateUI() {
    const displayName = (userProfile.name || '').trim() || 'مستخدم';
    document.getElementById('headerUserName').innerText = displayName;
    document.getElementById('headerAvatarChar').innerText = displayName.charAt(0) || "م";
    document.getElementById('profileBigName').innerText = displayName;
    document.getElementById('profileAvatarBig').innerText = displayName.charAt(0) || "م";
    
    document.getElementById('profStatWeight').innerText = `${userProfile.weight} كغم`;
    document.getElementById('profStatHeight').innerText = `${userProfile.height} سم`;
    document.getElementById('heroTargetCals').innerText = `${userProfile.targetCals} Kcal`;
    
    document.getElementById('headerUserGoal').innerText = 
      userProfile.goal === 'lose' ? 'تنشيف وعجز ذكي' : 
      userProfile.goal === 'gain' ? 'تضخيم وبناء عضلات' : 'ثبات الوزن والمحافظة';

    let totalCals = 0, totalP = 0, totalC = 0, totalF = 0;
    todayMeals.forEach(m => {
      totalCals += (m.calories || 0);
      totalP += (m.protein || 0);
      totalC += (m.carb || 0);
      totalF += (m.fat || 0);
    });

    const remCals = Math.max(0, userProfile.targetCals - totalCals);
    document.getElementById('remainingCalsText').innerText = remCals.toLocaleString();

    // تحديث دائرة القياس
    const circ = 2 * Math.PI * 50; // 314.15
    const pct = Math.min(1, totalCals / (userProfile.targetCals || 1));
    const offset = circ - (circ * pct);
    document.getElementById('calorieGaugeProgress').style.strokeDashoffset = offset;
    document.getElementById('calorieGaugeProgress').setAttribute('stroke', totalCals > userProfile.targetCals ? 'var(--orange-fire)' : 'var(--green-lime)');

    // الماكروز
    document.getElementById('heroProteinText').innerText = `${Math.round(totalP)} / ${userProfile.targetProtein}g`;
    document.getElementById('heroCarbText').innerText = `${Math.round(totalC)} / ${userProfile.targetCarb}g`;
    document.getElementById('heroFatText').innerText = `${Math.round(totalF)} / ${userProfile.targetFat}g`;

    document.getElementById('heroProteinBar').style.width = `${Math.min(100, (totalP / userProfile.targetProtein) * 100)}%`;
    document.getElementById('heroCarbBar').style.width = `${Math.min(100, (totalC / userProfile.targetCarb) * 100)}%`;
    document.getElementById('heroFatBar').style.width = `${Math.min(100, (totalF / userProfile.targetFat) * 100)}%`;

    // الماء والستريك
    document.getElementById('waterCounter').innerText = `${waterLiters.toFixed(1)} / 3L`;
    document.getElementById('streakCount').innerText = `${streakData.count} يوم`;
    document.getElementById('streakDaysView').innerText = `${streakData.count} يوم ستريك`;
    renderProStatus();
  }

  /* ================= عرض قائمة الوجبات ================= */
  function renderMealsList() {
    const container = document.getElementById('todayMealsContainer');
    container.innerHTML = '';

    if (todayMeals.length === 0) {
      container.innerHTML = `
        <div class="clean-card" style="text-align:center; padding:24px 14px; background:#FFFFFF;">
          <i class="fa-solid fa-bowl-food" style="font-size:2rem; color:var(--text-muted); margin-bottom:8px;"></i>
          <p style="font-size:0.78rem; font-weight:700; color:var(--text-secondary);">لم يتم تسجيل أي وجبة لليوم حتى الآن</p>
          <p style="font-size:0.65rem; color:var(--text-muted); margin-top:2px;">اضغط زر (+) بالأسفل لمسح صحنك بالكاميرا أو إدخالها يدوياً</p>
        </div>
      `;
      return;
    }

    const icons = ['🥗', '🍗', '🍚', '🍳', '🥑', '🥩', '🥪'];
    todayMeals.forEach((meal, idx) => {
      const card = document.createElement('div');
      card.className = 'floating-meal-card';
      const icon = icons[idx % icons.length];
      card.innerHTML = `
        <div class="meal-left">
          <div class="food-cutout">${icon}</div>
          <div class="meal-info">
            <h3>${escapeHtml(meal.name)}</h3>
            <p>بروتين ${meal.protein}g · كارب ${meal.carb}g · دهون ${meal.fat}g</p>
          </div>
        </div>
        <div class="meal-right">
          <span class="meal-cals">${meal.calories} Kcal</span>
          <button onclick="deleteMealItem(${idx})" class="quick-add-btn" style="background:#FEE2E2; color:#EF4444;" title="حذف">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>
      `;
      container.appendChild(card);
    });
  }

  function deleteMealItem(idx) {
    todayMeals.splice(idx, 1);
    saveTodayMeals();
    showToast("تم حذف الوجبة بنجاح");
  }

  /* ================= فحص الباركود والاتصال بالخادم ================= */
  function switchScannerMode(mode) {
    currentScanMode = mode;
    document.getElementById('btnModeFood').classList.toggle('active', mode === 'food');
    document.getElementById('btnModeBarcode').classList.toggle('active', mode === 'barcode');

    const statusText = document.getElementById('viewfinderStatusText');
    const manualBarcode = document.getElementById('manualBarcodeInputWrap');
    const mealNote = document.getElementById('mealNoteWrap');

    if (mode === 'barcode') {
      statusText.innerText = "وجّه الكاميرا نحو رمز الباركود للمنتج";
      manualBarcode.classList.remove('hidden');
      mealNote.classList.add('hidden');
    } else {
      statusText.innerText = "وجّه الكاميرا نحو طبقك أو الصحن";
      manualBarcode.classList.add('hidden');
      mealNote.classList.remove('hidden');
    }
  }

  function triggerScanAction() {
    if (currentScanMode === 'barcode') {
      const inputVal = document.getElementById('barcodeNumberInput').value.trim();
      if (inputVal) {
        searchBarcodeManual();
      } else {
        document.getElementById('cameraFileInput').click();
      }
    } else {
      document.getElementById('cameraFileInput').click();
    }
  }

  async function searchBarcodeManual() {
    if (!requirePro()) return;
    const code = document.getElementById('barcodeNumberInput').value.trim();
    if (!code) {
      showToast("يرجى كتابة رقم الباركود أولاً", "error");
      return;
    }
    showToast("جاري البحث عن المنتج في السجلات...", "info");

    try {
      const res = await proFetch(`/api/barcode/${encodeURIComponent(code)}`);
      const data = await res.json();

      if (res.ok && data.found) {
        currentBarcodeProduct = data.product;
        displayBarcodeResult(data.product);
      } else {
        openModal('barcodeNotFoundModal');
      }
    } catch (e) {
      if (e.handled) return;
      openModal('barcodeNotFoundModal');
    }
  }

  function displayBarcodeResult(prod) {
    document.getElementById('barcodeProdName').innerText = prod.name;
    document.getElementById('barcodeProdServing').innerText = `حجم الحصة: ${prod.serving || '100 جم'}`;
    document.getElementById('barcodeProdCals').innerText = prod.calories;
    document.getElementById('barcodeProdP').innerText = `${prod.protein}g`;
    document.getElementById('barcodeProdC').innerText = `${prod.carb}g`;

    const warningsWrap = document.getElementById('barcodeWarningsWrap');
    warningsWrap.innerHTML = '';
    (prod.warnings || []).forEach(w => {
      const badge = document.createElement('div');
      badge.style.cssText = "font-size:0.68rem; font-weight:700; padding:6px 10px; border-radius:8px; background:var(--orange-soft); color:var(--orange-fire);";
      badge.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> ${escapeHtml(w)}`;
      warningsWrap.appendChild(badge);
    });

    openModal('barcodeResultModal');
  }

  function addBarcodeMealToLog() {
    if (!currentBarcodeProduct) return;
    const prevTotals = getTotals();
    todayMeals.unshift({
      name: currentBarcodeProduct.name,
      calories: parseInt(currentBarcodeProduct.calories) || 0,
      protein: parseFloat(currentBarcodeProduct.protein) || 0,
      carb: parseFloat(currentBarcodeProduct.carb) || 0,
      fat: parseFloat(currentBarcodeProduct.fat) || 0,
      time: new Date().toLocaleTimeString('ar-IQ', { hour: '2-digit', minute: '2-digit' })
    });
    saveTodayMeals();
    closeModal('barcodeResultModal');
    switchMainTab('home');
    showToast("تم تسجيل المنتج المعلب بنجاح!");
    onMealAdded(prevTotals);
  }

  function openManualMealFromNotFound() {
    closeModal('barcodeNotFoundModal');
    openManualMealModal();
  }

  /* ================= مسح الصحن بالذكاء الاصطناعي (AI Lens) ================= */
  function handleFoodImageSelected(event) {
    const file = event.target.files[0];
    if (!file) return;

    capturedMime = file.type || 'image/jpeg';
    const reader = new FileReader();
    reader.onload = function(e) {
      capturedBase64Image = e.target.result.split(',')[1];
      const preview = document.getElementById('scannedFoodPreview');
      preview.src = e.target.result;
      preview.style.display = 'block';
      document.getElementById('viewfinderPrompt').style.display = 'none';

      if (currentScanMode === 'food') {
        analyzeFoodPhotoAI();
      } else {
        detectBarcodeFromFile(file);
      }
    };
    reader.readAsDataURL(file);
    event.target.value = '';
  }

  async function analyzeFoodPhotoAI() {
    if (!checkAIQuota()) return;
    if (!capturedBase64Image) return;

    showToast("جاري فحص الصحن وتقدير الجرامات بدقة...", "info");
    const note = document.getElementById('foodContextNote').value.trim();

    const prompt = `أنت خبير تغذية ورياضة متخصص. افحص بدقة هذا الصحن بناءً على ملاحظة المشترك: "${note}".
أرجع النتيجة بصيغة JSON حصرية ونظيفة بدون كود ماركداون إطلاقاً:
{
  "mealName": "اسم الوجبة",
  "calories": 420,
  "protein": 35,
  "carb": 40,
  "fat": 10,
  "description": "تقدير الجرامات والحصص الغذائية"
}`;

    try {
      const payload = {
        contents: [{ parts: [
          { text: prompt },
          { inline_data: { mime_type: capturedMime, data: capturedBase64Image } }
        ]}],
        generationConfig: { response_mime_type: "application/json" }
      };

      const res = await proFetch('/api/gemini/food', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ payload })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'خطأ في الخادم');
      const rawText = data.candidates[0].content.parts[0].text;
      const cleanJson = JSON.parse(rawText.replace(/```json/g, '').replace(/```/g, '').trim());

      currentAnalyzedFood = cleanJson;
      document.getElementById('resFoodName').innerText = cleanJson.mealName;
      document.getElementById('resFoodCals').innerText = `${cleanJson.calories} Kcal`;
      document.getElementById('resFoodDesc').innerText = cleanJson.description || '';
      document.getElementById('resFoodP').innerText = `${cleanJson.protein}g`;
      document.getElementById('resFoodC').innerText = `${cleanJson.carb}g`;
      document.getElementById('resFoodF').innerText = `${cleanJson.fat}g`;

      document.getElementById('aiFoodResultCard').classList.remove('hidden');
      consumeAIQuota();
      scheduleInterstitial();
    } catch(err) {
      if (!err.handled) showToast("تعذر تحليل الصورة: " + err.message, "error");
    }
  }

  function confirmAddScannedMeal() {
    if (!currentAnalyzedFood) return;
    const prevTotals = getTotals();
    todayMeals.unshift({
      name: currentAnalyzedFood.mealName,
      calories: parseInt(currentAnalyzedFood.calories) || 0,
      protein: parseFloat(currentAnalyzedFood.protein) || 0,
      carb: parseFloat(currentAnalyzedFood.carb) || 0,
      fat: parseFloat(currentAnalyzedFood.fat) || 0,
      time: new Date().toLocaleTimeString('ar-IQ', { hour: '2-digit', minute: '2-digit' })
    });
    saveTodayMeals();
    document.getElementById('aiFoodResultCard').classList.add('hidden');
    switchMainTab('home');
    showToast("تمت إضافة الطبق المحلل إلى سجل اليوم!");
    onMealAdded(prevTotals);
  }

  /* ================= إضافة وجبة يدوياً ================= */
  function openManualMealModal() {
    document.getElementById('manualMealName').value = '';
    document.getElementById('manualMealCals').value = '';
    document.getElementById('manualMealProtein').value = '';
    document.getElementById('manualMealCarb').value = '';
    document.getElementById('manualMealFat').value = '';
    openModal('manualMealModal');
  }

  function submitManualMeal() {
    const name = document.getElementById('manualMealName').value.trim() || 'وجبة مخصصة';
    const cals = parseInt(document.getElementById('manualMealCals').value) || 0;
    const p = parseFloat(document.getElementById('manualMealProtein').value) || 0;
    const c = parseFloat(document.getElementById('manualMealCarb').value) || 0;
    const f = parseFloat(document.getElementById('manualMealFat').value) || 0;

    if (cals <= 0 && p === 0 && c === 0 && f === 0) {
      showToast("يرجى كتابة السعرات أو الماكروز على الأقل", "error");
      return;
    }

    const prevTotals = getTotals();
    todayMeals.unshift({
      name: name,
      calories: cals || Math.round((p * 4) + (c * 4) + (f * 9)),
      protein: p,
      carb: c,
      fat: f,
      time: new Date().toLocaleTimeString('ar-IQ', { hour: '2-digit', minute: '2-digit' })
    });

    saveTodayMeals();
    closeModal('manualMealModal');
    switchMainTab('home');
    showToast("تم حفظ الوجبة اليدوية بنجاح!");
    onMealAdded(prevTotals);
  }

  /* ================= كورس التمارين الذكي والكورس الغذائي ================= */
  async function generateCustomWorkoutAI() {
    if (!checkAIQuota()) return;
    const waist = document.getElementById('inputWaist').value;
    const thigh = document.getElementById('inputThigh').value;
    const fatZones = document.getElementById('selectFatZones').value;
    const env = document.getElementById('selectWorkoutEnv').value;

    const btn = document.getElementById('btnGenerateWorkout');
    btn.disabled = true;
    showToast("جاري تصميم جدول التمارين والتكنيك المناسب لمقاساتك...", "info");

    const prompt = `أنت كابتن ومدرب لياقة بدنية محترف. صمم كورس تمارين أسبوعي شامل لمشترك بياناته:
- الطول: ${userProfile.height} سم | الوزن: ${userProfile.weight} كغم | الجنس: ${userProfile.gender}
- محيط الخصر: ${waist} سم | محيط الفخذ: ${thigh} سم
- مناطق تركز الدهون: ${fatZones}
- مكان ومعدات التمرين: ${env}
- هدفه: ${userProfile.goal}

المطلوب:
1. توزيع الأيام (مثال: Push / Pull / Legs أو Upper / Lower).
2. تحديد التمارين الموجهة لحرق الدهون في مناطق تركيزها وتقوية العضلات المقابلة.
3. التكرارات والجولات وتكنيك التنفس.`;

    try {
      const payload = { contents: [{ parts: [{ text: prompt }] }] };
      const res = await proFetch('/api/gemini/coach', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ payload })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'خطأ في الخادم');
      const text = data.candidates[0].content.parts[0].text;

      const box = document.getElementById('workoutResultBox');
      box.innerText = text;
      box.classList.remove('hidden');
      showToast("تم تصميم كورس التمارين بنجاح!");
      consumeAIQuota();
      scheduleInterstitial();
    } catch(e) {
      if (!e.handled) showToast("تعذر توليد الكورس: " + e.message, "error");
    } finally {
      btn.disabled = false;
    }
  }

  async function generateCustomDietAI() {
    if (!checkAIQuota()) return;
    const foods = document.getElementById('inputPantryFoods').value.trim();
    const budget = document.getElementById('selectPantryBudget').value;
    const mealsCount = document.getElementById('selectMealCount').value;

    if (!foods) {
      showToast("يرجى كتابة بعض الأطعمة المتوفرة لديك", "error");
      return;
    }

    const btn = document.getElementById('btnGenerateDiet');
    btn.disabled = true;
    showToast("جاري تنظيم الوجبات وتقسيم السعرات حسب طعامك...", "info");

    const prompt = `أنت أخصائي تغذية معتمد. صمم خطة غذائية يومية دقيقة بالجرامات للمشترك التالي:
- الهدف: ${userProfile.goal} | سعراته المستهدفة: ${userProfile.targetCals} ك.س | البروتين: ${userProfile.targetProtein} جم
- الأطعمة المتوفرة في بيته: ${foods}
- الميزانية: ${budget}
- نظام الوجبات: ${mealsCount}

المطلوب:
جدول يومي متكامل يحدد بالجرامات كمية الأكل لكل وجبة، مع حساب تقريبي للماكروز لكل وجبة واستغلال المكونات المتوفرة فقط.`;

    try {
      const payload = { contents: [{ parts: [{ text: prompt }] }] };
      const res = await proFetch('/api/gemini/diet', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ payload })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'خطأ في الخادم');
      const text = data.candidates[0].content.parts[0].text;

      const box = document.getElementById('dietResultBox');
      box.innerText = text;
      box.classList.remove('hidden');
      showToast("تم تصميم الخطة الغذائية بنجاح!");
      consumeAIQuota();
      scheduleInterstitial();
    } catch(e) {
      if (!e.handled) showToast("تعذر إكمال الخطة: " + e.message, "error");
    } finally {
      btn.disabled = false;
    }
  }

  /* ================= نظام الستريك والتحديات ================= */
  const CHALLENGES_KEY = 'fitsmart_challenges';
  function renderChallenges() {
    const list = document.getElementById('challengesListWrap');
    list.innerHTML = '';

    const defaultItems = [
      { text: "شرب 3 لتر ماء على مدار اليوم", done: waterLiters >= 3 },
      { text: "إكمال 8,000 خطوة أو تمرين 30 دقيقة", done: false },
      { text: "الامتناع التام عن السكر المكرر والمشروبات الغازية", done: false },
      { text: "تسجيل وجبات اليوم بدقة دون تجاوز السعرات", done: todayMeals.length >= 2 }
    ];

    let saved = null;
    try { saved = JSON.parse(localStorage.getItem(CHALLENGES_KEY)); } catch(e) {}
    const items = saved || defaultItems;

    items.forEach((c, idx) => {
      const row = document.createElement('div');
      row.style.cssText = `
        padding: 12px 14px;
        background: ${c.done ? 'var(--green-soft)' : 'var(--bg-subtle)'};
        border: 1px solid ${c.done ? 'rgba(34,197,94,0.3)' : 'var(--border)'};
        border-radius: var(--radius-md);
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
        transition: all 0.2s;
      `;
      row.onclick = () => toggleChallengeItem(idx, items);

      row.innerHTML = `
        <span style="font-size:0.76rem; font-weight:700; color:${c.done ? 'var(--green-lime)' : 'var(--text-primary)'}; ${c.done ? 'text-decoration:line-through;' : ''}">
          ${c.text}
        </span>
        <i class="fa-solid ${c.done ? 'fa-circle-check' : 'fa-circle'}" style="color:${c.done ? 'var(--green-lime)' : 'var(--text-muted)'}; font-size:1.1rem;"></i>
      `;
      list.appendChild(row);
    });
  }

  function toggleChallengeItem(idx, items) {
    items[idx].done = !items[idx].done;
    localStorage.setItem(CHALLENGES_KEY, JSON.stringify(items));
    renderChallenges();

    const allDone = items.every(i => i.done);
    const todayCycle = get7AMCycleDate(new Date());
    if (allDone && streakData.lastCompletedDate !== todayCycle) {
      streakData.lastCompletedDate = todayCycle;
      streakData.count += 1;
      saveStreak();
      showToast("🔥 رائع جداً! أكملت كل تحديات اليوم وارتفعت شعلة الستريك!", "success");
    }
  }

  function addWaterCup() {
    waterLiters = Math.round((waterLiters + 0.25) * 100) / 100;
    localStorage.setItem('fitsmart_water', waterLiters);
    updateUI();
    showToast(`💧 تم شرب 250 مل (+كوب ماء)`);
  }

  function showStreakInfo() {
    showToast(`🔥 شعلتك مشتعلة منذ ${streakData.count} يوم! يرست السجل 7:00 ص.`);
  }

  /* ================= تفعيل اشتراك PRO بالأكواد ================= */
  let selectedSub = 'monthly';
  function selectSubOption(type) {
    selectedSub = type;
    document.getElementById('optMonthly').classList.toggle('selected', type === 'monthly');
    document.getElementById('optYearly').classList.toggle('selected', type === 'yearly');
  }

  async function redeemActivationCode() {
    const code = document.getElementById('activationCodeInput').value.trim();
    if (!code) {
      showToast("يرجى كتابة كود التفعيل المكون من 4 رموز", "error");
      return;
    }

    try {
      const res = await fetch('/api/subscription/redeem', {
        method: 'POST',
        headers: proHeaders(),
        body: JSON.stringify({ code })
      });
      const data = await res.json();

      if (res.ok && data.success) {
        setProState({ token: data.token, expiresMs: data.expires_at_ms, type: data.type });
        applyProState(true, data.expires_at_ms);
        document.getElementById('activationCodeInput').value = '';
        saveProfile();
        closeModal('proSubscriptionModal');
        showToast(`🎉 ${data.message}`);
      } else {
        showToast(data.error || "كود التفعيل غير صالح", "error");
      }
    } catch(e) {
      showToast("تعذر التحقق من الكود حالياً", "error");
    }
  }

  /* ================= التنقل بين التبويبات ================= */
  function switchMainTab(tab) {
    ['viewHome', 'viewCamera', 'viewWorkouts', 'viewAnalytics', 'viewProfile'].forEach(v => {
      document.getElementById(v).classList.add('hidden');
    });

    ['dockBtnHome', 'dockBtnWorkouts', 'dockBtnAnalytics', 'dockBtnProfile'].forEach(b => {
      const el = document.getElementById(b);
      if (el) el.classList.remove('active');
    });

    const fab = document.getElementById('mainFabBtn');
    const menu = document.getElementById('fabMenu');
    fab.classList.remove('open');
    menu.classList.remove('show');

    if (tab === 'home') {
      document.getElementById('viewHome').classList.remove('hidden');
      document.getElementById('dockBtnHome').classList.add('active');
    } else if (tab === 'workouts') {
      document.getElementById('viewWorkouts').classList.remove('hidden');
      document.getElementById('dockBtnWorkouts').classList.add('active');
    } else if (tab === 'analytics') {
      document.getElementById('viewAnalytics').classList.remove('hidden');
      document.getElementById('dockBtnAnalytics').classList.add('active');
    } else if (tab === 'profile') {
      document.getElementById('viewProfile').classList.remove('hidden');
      document.getElementById('dockBtnProfile').classList.add('active');
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function openCameraView(mode) {
    toggleFabMenu();
    if (mode === 'barcode' && !requirePro()) return;
    ['viewHome', 'viewWorkouts', 'viewAnalytics', 'viewProfile'].forEach(v => document.getElementById(v).classList.add('hidden'));
    document.getElementById('viewCamera').classList.remove('hidden');
    switchScannerMode(mode);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function toggleFabMenu() {
    const fab = document.getElementById('mainFabBtn');
    const menu = document.getElementById('fabMenu');
    fab.classList.toggle('open');
    menu.classList.toggle('show');
  }

  /* ================= النوافذ وإدارة الـ Modals ================= */
  function openModal(id) { document.getElementById(id).classList.add('show'); }
  function closeModal(id) { document.getElementById(id).classList.remove('show'); }

  function openProModal(e) {
    if (e) e.stopPropagation();
    openModal('proSubscriptionModal');
  }

  function openProfileModal() {
    document.getElementById('editUserName').value = userProfile.name;
    document.getElementById('editUserWeight').value = userProfile.weight;
    document.getElementById('editUserHeight').value = userProfile.height;
    document.getElementById('editUserAge').value = userProfile.age;
    document.getElementById('editUserGender').value = userProfile.gender;
    document.getElementById('editUserGoal').value = userProfile.goal;
    openModal('profileModal');
  }

  function saveProfileChanges() {
    userProfile.name = document.getElementById('editUserName').value.trim() || 'مشترك';
    userProfile.weight = parseFloat(document.getElementById('editUserWeight').value) || 75;
    userProfile.height = parseFloat(document.getElementById('editUserHeight').value) || 175;
    userProfile.age = parseFloat(document.getElementById('editUserAge').value) || 23;
    userProfile.gender = document.getElementById('editUserGender').value;
    userProfile.goal = document.getElementById('editUserGoal').value;

    recalculateTargets();
    closeModal('profileModal');
    showToast("تم حفظ وتحديث بيانات الجسم والاحتياج اليومي!");
  }

  /* ================= إشعارات Toast ================= */
  function showToast(msg, type = 'info') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = 'clean-toast';
    const icon = type === 'error' ? 'fa-circle-xmark' : (type === 'success' ? 'fa-circle-check' : 'fa-bell');
    const color = type === 'error' ? '#EF4444' : (type === 'success' ? 'var(--green-lime)' : 'var(--blue-sport)');
    toast.innerHTML = `<i class="fa-solid ${icon}" style="color:${color}; font-size:1.1rem;"></i><span>${msg}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.transition = 'opacity 0.3s, transform 0.3s';
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(-10px)';
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  }

  /* ================= أدوات مساعدة ================= */
  function escapeHtml(str) {
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  /* ================= التسجيل الأولي ================= */
  function completeOnboarding() {
    const name = document.getElementById('obName').value.trim();
    const weight = parseFloat(document.getElementById('obWeight').value);
    const height = parseFloat(document.getElementById('obHeight').value);
    const age = parseFloat(document.getElementById('obAge').value);

    if (!name) { showToast("يرجى كتابة اسمك", "error"); return; }
    if (!(weight >= 20 && weight <= 300)) { showToast("يرجى إدخال وزن صحيح (20 - 300 كغم)", "error"); return; }
    if (!(height >= 100 && height <= 250)) { showToast("يرجى إدخال طول صحيح (100 - 250 سم)", "error"); return; }
    if (!(age >= 10 && age <= 100)) { showToast("يرجى إدخال عمر صحيح (10 - 100)", "error"); return; }

    userProfile.name = name;
    userProfile.weight = weight;
    userProfile.height = height;
    userProfile.age = age;
    userProfile.gender = document.getElementById('obGender').value;
    userProfile.goal = document.getElementById('obGoal').value;

    localStorage.setItem('fitsmart_onboarded', '1');
    recalculateTargets();
    updateUI();
    closeModal('onboardingModal');
    showToast(`🎉 أهلاً ${name}! تم حساب احتياجك اليومي.`, "success");
  }

  /* ================= حد استخدام الذكاء الاصطناعي للمستخدم العادي ================= */
  const AI_DAILY_LIMIT = 5;
  const AI_USAGE_KEY = 'fitsmart_ai_usage';

  function getAIUsage() {
    const cycle = get7AMCycleDate(new Date());
    let u = null;
    try { u = JSON.parse(localStorage.getItem(AI_USAGE_KEY)); } catch(e) {}
    if (!u || u.cycle !== cycle) u = { cycle, count: 0 };
    return u;
  }
  function getAIRemaining() {
    return Math.max(0, AI_DAILY_LIMIT - getAIUsage().count);
  }
  // يُستدعى قبل أي ميزة ذكاء اصطناعي: المشترك (أو التجربة) بلا حد، والعادي 5 باليوم
  function checkAIQuota() {
    enforceProExpiry();
    if (userProfile.isPro) return true;
    if (getAIRemaining() <= 0) {
      showToast(`وصلت للحد اليومي (${AI_DAILY_LIMIT} استخدامات للذكاء الاصطناعي). يتجدد الساعة 7:00 ص أو اشترك في PRO لاستخدام بلا حدود.`, "error");
      openModal('proSubscriptionModal');
      return false;
    }
    return true;
  }
  function consumeAIQuota() {
    if (userProfile.isPro) return;
    const u = getAIUsage();
    u.count += 1;
    localStorage.setItem(AI_USAGE_KEY, JSON.stringify(u));
    renderProStatus();
  }

  /* ================= تحذير بلوغ الحد من السعرات والماكروز ================= */
  let pendingAdAfterWarning = false;

  function getTotals() {
    const t = { cals: 0, p: 0, c: 0, f: 0 };
    todayMeals.forEach(m => {
      t.cals += (m.calories || 0);
      t.p += (m.protein || 0);
      t.c += (m.carb || 0);
      t.f += (m.fat || 0);
    });
    return t;
  }

  function checkIntakeLimits(prev) {
    const now = getTotals();
    const defs = [
      { k: 'cals', label: 'السعرات', unit: 'سعرة', target: userProfile.targetCals },
      { k: 'p', label: 'البروتين', unit: 'غ', target: userProfile.targetProtein },
      { k: 'c', label: 'الكربوهيدرات', unit: 'غ', target: userProfile.targetCarb },
      { k: 'f', label: 'الدهون', unit: 'غ', target: userProfile.targetFat }
    ];
    const msgs = [];
    defs.forEach(d => {
      if (!(d.target > 0)) return;
      const crossed = prev[d.k] < d.target && now[d.k] >= d.target;
      const stillOverCals = d.k === 'cals' && prev[d.k] >= d.target && now[d.k] > prev[d.k];
      if (!crossed && !stillOverCals) return;
      const verb = now[d.k] > d.target ? 'تجاوزت' : 'بلغت';
      msgs.push(`${verb} الحد اليومي من ${d.label}: ${Math.round(now[d.k])} / ${Math.round(d.target)} ${d.unit}`);
    });
    if (!msgs.length) return false;

    document.getElementById('limitWarningList').innerHTML = msgs
      .map(m => `<div class="limit-warn-row"><i class="fa-solid fa-triangle-exclamation"></i><span>${m}</span></div>`)
      .join('');
    openModal('limitWarningModal');
    return true;
  }

  function closeLimitWarning() {
    closeModal('limitWarningModal');
    if (pendingAdAfterWarning) {
      pendingAdAfterWarning = false;
      scheduleInterstitial(400);
    }
  }

  // بعد إكمال إدخال وجبة: تحذير إن لزم، ثم الإعلان البيني
  function onMealAdded(prev) {
    const warned = checkIntakeLimits(prev);
    if (warned) pendingAdAfterWarning = true;
    else scheduleInterstitial();
  }

  /* ================= الإعلان البيني (AdMob - شاشة كاملة) ================= */
  const ADMOB_INTERSTITIAL_ID = 'ca-app-pub-1960600515170601/7775727781';
  const AD_MIN_GAP_MS = 60000; // أقل فاصل بين إعلانين (بالميلي ثانية)
  let adLastShown = 0, adShowing = false, adTimer = null;

  function getAdBridge() {
    const cap = window.Capacitor && window.Capacitor.Plugins && window.Capacitor.Plugins.AdMob;
    if (cap) return { type: 'capacitor', plugin: cap };
    const a = window.AndroidAds || window.Android || window.AndroidBridge;
    if (a && typeof a.showInterstitial === 'function') return { type: 'android', plugin: a };
    return null; // متصفح عادي: لا يوجد إعلان
  }

  async function initAds() {
    const b = getAdBridge();
    if (!b || b.type !== 'capacitor') return;
    try {
      await b.plugin.initialize({ initializeForTesting: false });
      await b.plugin.prepareInterstitial({ adId: ADMOB_INTERSTITIAL_ID });
    } catch(e) { console.warn('AdMob init failed', e); }
  }

  async function showInterstitialAd() {
    if (userProfile.isPro || adShowing) return;            // لا إعلانات للمشتركين
    if (Date.now() - adLastShown < AD_MIN_GAP_MS) return;  // منع تكرار الإعلانات
    const b = getAdBridge();
    if (!b) return;
    adShowing = true;
    try {
      if (b.type === 'capacitor') {
        try {
          await b.plugin.showInterstitial();
        } catch(e) {
          await b.plugin.prepareInterstitial({ adId: ADMOB_INTERSTITIAL_ID });
          await b.plugin.showInterstitial();
        }
        adLastShown = Date.now();
        b.plugin.prepareInterstitial({ adId: ADMOB_INTERSTITIAL_ID }).catch(() => {}); // تجهيز الإعلان التالي
      } else {
        b.plugin.showInterstitial();
        adLastShown = Date.now();
      }
    } catch(e) {
      console.warn('Interstitial failed', e);
    } finally {
      adShowing = false;
    }
  }

  function scheduleInterstitial(delay) {
    clearTimeout(adTimer);
    adTimer = setTimeout(showInterstitialAd, typeof delay === 'number' ? delay : 900);
  }

  /* ================= الستريك: كسر السلسلة عند تفويت يوم ================= */
  function checkStreakContinuity() {
    const last = streakData.lastCompletedDate;
    if (!last) return;
    const today = get7AMCycleDate(new Date());
    const yesterday = get7AMCycleDate(new Date(Date.now() - 86400000));
    if (last !== today && last !== yesterday && streakData.count > 0) {
      streakData.count = 0;
      localStorage.setItem('fitsmart_streak', JSON.stringify(streakData));
    }
  }

  /* ================= قراءة الباركود من الصورة (إن دعمها الجهاز) ================= */
  async function detectBarcodeFromFile(file) {
    if (!('BarcodeDetector' in window)) {
      showToast("جهازك لا يدعم قراءة الباركود من الصورة، اكتب الرقم يدوياً.", "info");
      return;
    }
    try {
      const bmp = await createImageBitmap(file);
      const results = await new BarcodeDetector().detect(bmp);
      if (results.length && results[0].rawValue) {
        document.getElementById('barcodeNumberInput').value = results[0].rawValue;
        searchBarcodeManual();
      } else {
        showToast("لم نتمكن من قراءة الباركود، جرّب صورة أوضح أو اكتب الرقم.", "error");
      }
    } catch(e) {
      showToast("تعذرت قراءة الباركود، اكتب الرقم يدوياً.", "error");
    }
  }

  // تشغيل أولي عند تحميل الصفحة
  
  /* ================= التجربة المجانية لمدة 7 أيام ================= */
  async function startFreeTrial() {
    if (userProfile.isPro) {
      showToast("اشتراكك فعّال بالفعل.", "info");
      return;
    }
    try {
      const res = await fetch('/api/subscription/trial', {
        method: 'POST',
        headers: proHeaders(),
        body: '{}'
      });
      const data = await res.json();
      if (res.ok && data.success) {
        setProState({ token: data.token, expiresMs: data.expires_at_ms, type: 'trial' });
        applyProState(true, data.expires_at_ms);
        saveProfile();
        closeModal('proSubscriptionModal');
        showToast(`🎉 ${data.message}`, "success");
      } else {
        showToast(data.error || "تعذر تفعيل التجربة المجانية", "error");
      }
    } catch(e) {
      showToast("تعذر تفعيل التجربة حالياً", "error");
    }
  }

  window.addEventListener('DOMContentLoaded', loadInitialData);
</script>
</body>
</html>
