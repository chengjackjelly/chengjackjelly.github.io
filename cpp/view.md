What are the performance benefits with using STL Ranges/Views rather than [2p]
STL algorithms? Are there other benefits besides performance? Explain

a view never copies any elements, nor does it
keep track of which elements it is pointing to (as the
image might suggest). Instead, a view is computed lazily.

views are lightweight objects that refer to elements they do not own2
views are O(1) copyable and assignable