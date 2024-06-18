import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from flask import url_for
# Function to generate the welcome animation
def generate_welcome_animation(app_root_path):
    fig, ax = plt.subplots(figsize=(4, 2))  
    fig.patch.set_facecolor('cadetblue')  
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')  

    text = ax.text(0.5, 0.5, "", fontsize=30, ha='center')

    def update(frame):
        if frame < 100:
            alpha = frame / 100
            text.set_text("Welcome")
            text.set_alpha(alpha)
        else:
            text.set_text("Welcome")
            text.set_alpha(1)
        return text,

    anim = FuncAnimation(fig, update, frames=200, interval=30)
    
    animation_dir = os.path.join(app_root_path, 'static', 'assets', 'animation')
    if not os.path.exists(animation_dir):
        os.makedirs(animation_dir)

    gif_path = os.path.join(animation_dir, 'welcome_animation.gif')
    if not os.path.exists(gif_path):  
        anim.save(gif_path, writer='pillow')

    plt.close(fig)

    return url_for('static', filename='assets/animation/welcome_animation.gif')