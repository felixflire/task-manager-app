# tasksapp/ml_summary.py
from datetime import date

def analyze_patterns(all_tasks):
    total     = all_tasks.count()
    completed = all_tasks.filter(completed="completed").count()
    
    if total == 0:
        avg_completion = 0
    else:
        avg_completion = (completed / total) * 100

    common_words = {}
    for task in all_tasks:
        for word in task.tasksfield.lower().split():
            if len(word) > 3:
                common_words[word] = common_words.get(word, 0) + 1

    most_common = max(common_words, key=common_words.get) if common_words else "general"

    return {
        "avg_completion": avg_completion,
        "most_common_task": most_common,
        "total_ever": total,
        "completed_ever": completed
    }


def generate_summary(todays_tasks, all_tasks):
    today     = date.today().strftime("%B %d, %Y")
    total     = todays_tasks.count()
    completed = todays_tasks.filter(completed="completed").count()
    pending   = total - completed
    score     = (completed / total * 100) if total > 0 else 0

    patterns = analyze_patterns(all_tasks)
    avg      = patterns["avg_completion"]
    common   = patterns["most_common_task"]

    if total == 0:
        return f"📅 {today}\n\nNo tasks added today.\nYour most common task type is '{common}'."

    if score > avg:
        performance = f"You are performing ABOVE your usual average of {avg:.0f}%. Great effort!"
    elif score == avg:
        performance = f"You are performing at your usual average of {avg:.0f}%. Stay consistent!"
    else:
        performance = f"You are performing BELOW your usual average of {avg:.0f}%. Push harder!"

    if score == 100:
        mood = "Perfect day! Every task completed."
    elif score >= 70:
        mood = "Good progress today. Almost there!"
    elif score >= 40:
        mood = "Decent effort. Try to clear the remaining tasks."
    else:
        mood = "Slow day. Focus on your top priority tomorrow."

    # ✅ use \n explicitly instead of multiline f-string
    lines = [
        f"📅 Daily Summary — {today}",
        "",
        f"📋 Total Tasks   : {total}",
        f"✅ Completed     : {completed}",
        f"⏳ Pending       : {pending}",
        f"📊 Today Score   : {score:.0f}%",
        f"📈 Your Average  : {avg:.0f}%",
        f"🏷️ Your Top Task : {common}",
        "",
        f"💬 {mood}",
        f"📌 {performance}",
    ]

    pending_tasks = todays_tasks.exclude(completed="completed")
    if pending_tasks.exists():
        lines.append("")
        lines.append("⏳ Still Pending:")
        for task in pending_tasks:
            lines.append(f"   - {task.tasksfield}: {task.description}")

    done_tasks = todays_tasks.filter(completed="completed")
    if done_tasks.exists():
        lines.append("")
        lines.append("✅ Completed:")
        for task in done_tasks:
            lines.append(f"   - {task.tasksfield}: {task.description}")

    lines += [
        "",
        "📊 All Time Stats:",
        f"   Total tasks ever  : {patterns['total_ever']}",
        f"   Completed ever    : {patterns['completed_ever']}",
        f"   Completion rate   : {avg:.0f}%",
    ]

    return "\n".join(lines)  # ✅ joins with real line breaks