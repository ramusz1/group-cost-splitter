# cost_master
splits costs within a group using minimal number of transactions


reads data in the following format:
group <members divided with space>
who_paid amount
or 
who_ows -amount
or
who_paid amount even
the last one means that one person paid for everyone in the group and the debt is split evenly

