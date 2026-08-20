"""
Generate a clear, easy-to-understand figure explaining keyword, semantic, and hybrid search.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(16, 6))
fig.suptitle('Search Types Explained: Keyword vs. Semantic vs. Hybrid', 
             fontsize=18, fontweight='bold', y=0.98)

# ============================================================================
# Panel 1: Keyword Search
# ============================================================================
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Keyword Search', fontsize=14, fontweight='bold', pad=20)

# Query box
query_box = FancyBboxPatch((0.5, 8), 9, 1.2, boxstyle="round,pad=0.1", 
                           edgecolor='#2E86AB', facecolor='#E8F4F8', linewidth=2)
ax1.add_patch(query_box)
ax1.text(5, 8.6, 'Query: "unblinding clinical trial"', ha='center', va='center', 
         fontsize=11, fontweight='bold')

# Arrow
arrow1 = FancyArrowPatch((5, 7.8), (5, 6.8), arrowstyle='->', 
                        mutation_scale=30, linewidth=2.5, color='#2E86AB')
ax1.add_patch(arrow1)

# Process label
ax1.text(5, 7.2, 'Exact word matching', ha='center', fontsize=10, 
         style='italic', color='#555555')

# Document boxes - matching keywords
docs = [
    ("Doc 1: Clinical trial unblinding\noccurred during week 3", True, 5.2),
    ("Doc 2: The patient discovered\ntreatment assignment", False, 3.5),
    ("Doc 3: Unblinding study design\nprotocol", True, 1.8),
]

for doc_text, match, y_pos in docs:
    color = '#90EE90' if match else '#FFB6B6'
    edge_color = '#2D5016' if match else '#8B0000'
    doc_box = FancyBboxPatch((0.5, y_pos-0.5), 9, 1, boxstyle="round,pad=0.05", 
                             edgecolor=edge_color, facecolor=color, linewidth=2)
    ax1.add_patch(doc_box)
    ax1.text(5, y_pos, doc_text, ha='center', va='center', fontsize=9)
    
    # Match indicator
    indicator = '✓ MATCH' if match else '✗ NO MATCH'
    ax1.text(9.5, y_pos, indicator, ha='left', va='center', fontsize=8, 
             fontweight='bold', color=edge_color)

# Bottom explanation
ax1.text(5, 0.5, 'Looks for exact words\nMissing context & synonyms', 
         ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='#FFF9E6', 
         edgecolor='#FFB84D', linewidth=2), style='italic')

# ============================================================================
# Panel 2: Semantic Search
# ============================================================================
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Semantic Search', fontsize=14, fontweight='bold', pad=20)

# Query box
query_box2 = FancyBboxPatch((0.5, 8), 9, 1.2, boxstyle="round,pad=0.1", 
                            edgecolor='#A23B72', facecolor='#F8E8F4', linewidth=2)
ax2.add_patch(query_box2)
ax2.text(5, 8.6, 'Query: "unblinding clinical trial"', ha='center', va='center', 
         fontsize=11, fontweight='bold')

# Arrow
arrow2 = FancyArrowPatch((5, 7.8), (5, 6.8), arrowstyle='->', 
                        mutation_scale=30, linewidth=2.5, color='#A23B72')
ax2.add_patch(arrow2)

# Embedding step
embedding_box = FancyBboxPatch((0.5, 6.3), 9, 0.5, boxstyle="round,pad=0.05", 
                               edgecolor='#A23B72', facecolor='#E8D4E8', linewidth=1.5)
ax2.add_patch(embedding_box)
ax2.text(5, 6.55, '🧠 Convert to vector embedding [1024-dim]', ha='center', va='center', 
         fontsize=9, fontweight='bold')

# Arrow
arrow2b = FancyArrowPatch((5, 6.2), (5, 5.2), arrowstyle='->', 
                         mutation_scale=30, linewidth=2.5, color='#A23B72')
ax2.add_patch(arrow2b)

# Process label
ax2.text(5, 5.7, 'Cosine similarity in\nembedding space', ha='center', fontsize=10, 
         style='italic', color='#555555')

# Document boxes - semantic matching
docs_semantic = [
    ("Doc 1: Clinical trial unblinding\noccurred during week 3", 0.95, 5.0),
    ("Doc 2: The patient discovered\ntreatment assignment", 0.82, 3.3),
    ("Doc 3: Inadvertent exposure of\ntreatment allocation", 0.88, 1.6),
]

for doc_text, score, y_pos in docs_semantic:
    # Color based on similarity score
    if score > 0.85:
        color = '#90EE90'
        edge_color = '#2D5016'
    elif score > 0.75:
        color = '#FFFFE0'
        edge_color = '#8B8B00'
    else:
        color = '#FFB6B6'
        edge_color = '#8B0000'
    
    doc_box = FancyBboxPatch((0.5, y_pos-0.5), 7.5, 1, boxstyle="round,pad=0.05", 
                             edgecolor=edge_color, facecolor=color, linewidth=2)
    ax2.add_patch(doc_box)
    ax2.text(4, y_pos, doc_text, ha='center', va='center', fontsize=9)
    
    # Similarity score
    ax2.text(8.3, y_pos, f'{score:.2f}', ha='center', va='center', fontsize=9, 
             fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', 
             edgecolor=edge_color, linewidth=1.5))

# Bottom explanation
ax2.text(5, 0.5, 'Understands meaning & context\nCaptures synonyms & similar concepts', 
         ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='#FFF9E6', 
         edgecolor='#FFB84D', linewidth=2), style='italic')

# ============================================================================
# Panel 3: Hybrid Search
# ============================================================================
ax3 = axes[2]
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.axis('off')
ax3.set_title('Hybrid Search', fontsize=14, fontweight='bold', pad=20)

# Query box
query_box3 = FancyBboxPatch((0.5, 8), 9, 1.2, boxstyle="round,pad=0.1", 
                            edgecolor='#F18F01', facecolor='#F8F0E8', linewidth=2)
ax3.add_patch(query_box3)
ax3.text(5, 8.6, 'Query: "unblinding clinical trial"', ha='center', va='center', 
         fontsize=11, fontweight='bold')

# Split arrow
arrow3a = FancyArrowPatch((3.5, 7.8), (2, 6.8), arrowstyle='->', 
                         mutation_scale=25, linewidth=2.5, color='#2E86AB')
ax3.add_patch(arrow3a)
arrow3b = FancyArrowPatch((6.5, 7.8), (8, 6.8), arrowstyle='->', 
                         mutation_scale=25, linewidth=2.5, color='#A23B72')
ax3.add_patch(arrow3b)

# Two parallel paths
kw_box = FancyBboxPatch((0.2, 6.2), 3.5, 0.6, boxstyle="round,pad=0.05", 
                        edgecolor='#2E86AB', facecolor='#E8F4F8', linewidth=1.5)
ax3.add_patch(kw_box)
ax3.text(2, 6.5, 'Keyword Match', ha='center', va='center', 
         fontsize=9, fontweight='bold')

sem_box = FancyBboxPatch((6.3, 6.2), 3.5, 0.6, boxstyle="round,pad=0.05", 
                         edgecolor='#A23B72', facecolor='#F8E8F4', linewidth=1.5)
ax3.add_patch(sem_box)
ax3.text(8, 6.5, 'Semantic Match', ha='center', va='center', 
         fontsize=9, fontweight='bold')

# Converge arrows
arrow3c = FancyArrowPatch((2, 6.1), (4.5, 5.2), arrowstyle='->', 
                         mutation_scale=25, linewidth=2.5, color='#2E86AB')
ax3.add_patch(arrow3c)
arrow3d = FancyArrowPatch((8, 6.1), (5.5, 5.2), arrowstyle='->', 
                         mutation_scale=25, linewidth=2.5, color='#A23B72')
ax3.add_patch(arrow3d)

# Merge box
merge_box = FancyBboxPatch((2, 4.5), 6, 0.7, boxstyle="round,pad=0.05", 
                           edgecolor='#F18F01', facecolor='#F8F0E8', linewidth=2)
ax3.add_patch(merge_box)
ax3.text(5, 4.85, '⚡ Combine & Rank Results', ha='center', va='center', 
         fontsize=10, fontweight='bold')

# Arrow down
arrow3e = FancyArrowPatch((5, 4.4), (5, 3.3), arrowstyle='->', 
                         mutation_scale=30, linewidth=2.5, color='#F18F01')
ax3.add_patch(arrow3e)

# Final results
final_box = FancyBboxPatch((0.5, 2.3), 9, 1, boxstyle="round,pad=0.05", 
                           edgecolor='#2D5016', facecolor='#E0FFE0', linewidth=2)
ax3.add_patch(final_box)
ax3.text(5, 2.8, '✓ Best of both worlds:\nExact matches + semantic understanding', 
         ha='center', va='center', fontsize=9, fontweight='bold')

# Bottom explanation
ax3.text(5, 0.8, 'Highest precision & recall\nBalances specificity with meaning', 
         ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='#FFF9E6', 
         edgecolor='#FFB84D', linewidth=2), style='italic')

plt.tight_layout()
plt.savefig('search_types_visualization.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✓ Figure saved as 'search_types_visualization.png'")
plt.show()
