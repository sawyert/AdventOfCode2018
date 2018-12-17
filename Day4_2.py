input = """
[1518-06-05 00:46] falls asleep
[1518-06-27 00:21] falls asleep
[1518-11-10 23:52] Guard #881 begins shift
[1518-11-08 00:51] wakes up
[1518-04-23 00:58] wakes up
[1518-05-14 00:40] falls asleep
[1518-07-08 00:57] wakes up
[1518-09-03 00:02] Guard #911 begins shift
[1518-06-13 00:45] falls asleep
[1518-10-07 23:58] Guard #239 begins shift
[1518-06-12 23:59] Guard #1021 begins shift
[1518-08-03 23:59] Guard #877 begins shift
[1518-06-23 00:02] Guard #1021 begins shift
[1518-10-06 00:50] wakes up
[1518-11-15 00:03] Guard #613 begins shift
[1518-03-21 00:34] wakes up
[1518-06-27 00:51] falls asleep
[1518-05-14 00:54] wakes up
[1518-03-24 00:38] wakes up
[1518-03-29 00:26] falls asleep
[1518-05-29 00:19] falls asleep
[1518-04-16 23:50] Guard #571 begins shift
[1518-03-06 00:43] falls asleep
[1518-04-06 00:10] falls asleep
[1518-04-08 00:09] falls asleep
[1518-07-22 00:54] wakes up
[1518-08-01 00:59] wakes up
[1518-05-13 00:26] falls asleep
[1518-05-09 00:55] wakes up
[1518-09-16 00:12] wakes up
[1518-07-13 00:01] Guard #3539 begins shift
[1518-06-27 00:25] wakes up
[1518-10-04 00:37] falls asleep
[1518-08-01 00:45] falls asleep
[1518-07-23 00:18] wakes up
[1518-09-01 00:36] falls asleep
[1518-09-25 00:26] falls asleep
[1518-04-05 00:19] falls asleep
[1518-07-01 00:09] falls asleep
[1518-07-05 00:51] wakes up
[1518-03-20 00:55] wakes up
[1518-04-21 00:21] falls asleep
[1518-06-15 23:59] Guard #2441 begins shift
[1518-08-20 00:02] Guard #887 begins shift
[1518-05-03 00:15] falls asleep
[1518-09-18 00:09] falls asleep
[1518-07-15 00:16] falls asleep
[1518-03-30 23:48] Guard #1249 begins shift
[1518-10-26 00:45] wakes up
[1518-04-20 00:09] falls asleep
[1518-03-12 00:44] wakes up
[1518-11-13 00:29] wakes up
[1518-06-22 00:56] wakes up
[1518-04-13 00:13] falls asleep
[1518-08-21 00:51] falls asleep
[1518-04-13 00:02] Guard #1607 begins shift
[1518-10-21 23:46] Guard #239 begins shift
[1518-07-02 00:37] falls asleep
[1518-09-17 00:02] Guard #2963 begins shift
[1518-09-22 00:37] wakes up
[1518-04-05 00:02] Guard #613 begins shift
[1518-10-12 00:49] falls asleep
[1518-05-11 00:36] wakes up
[1518-08-10 00:12] falls asleep
[1518-08-01 00:41] wakes up
[1518-04-23 00:04] falls asleep
[1518-04-13 00:41] wakes up
[1518-07-10 00:29] falls asleep
[1518-10-19 00:57] wakes up
[1518-08-12 00:58] wakes up
[1518-06-02 00:00] falls asleep
[1518-04-21 00:58] wakes up
[1518-09-20 00:43] wakes up
[1518-10-19 00:19] falls asleep
[1518-08-05 00:25] wakes up
[1518-11-22 23:57] Guard #2963 begins shift
[1518-04-06 00:04] Guard #1877 begins shift
[1518-05-26 00:48] wakes up
[1518-06-23 00:54] wakes up
[1518-07-08 00:54] falls asleep
[1518-05-18 00:17] falls asleep
[1518-04-30 00:21] falls asleep
[1518-03-03 00:57] wakes up
[1518-07-20 00:04] falls asleep
[1518-08-27 00:39] wakes up
[1518-07-10 23:50] Guard #887 begins shift
[1518-08-25 00:02] Guard #1607 begins shift
[1518-04-15 00:54] falls asleep
[1518-10-03 00:45] wakes up
[1518-04-25 00:47] wakes up
[1518-09-08 00:26] falls asleep
[1518-06-15 00:18] falls asleep
[1518-09-09 00:41] wakes up
[1518-11-14 00:00] Guard #2207 begins shift
[1518-05-01 00:49] falls asleep
[1518-11-03 00:50] wakes up
[1518-07-18 00:26] falls asleep
[1518-07-07 00:30] falls asleep
[1518-06-27 00:41] wakes up
[1518-09-07 00:04] falls asleep
[1518-06-30 23:57] Guard #239 begins shift
[1518-09-14 00:56] wakes up
[1518-05-09 00:18] falls asleep
[1518-06-03 00:02] Guard #2441 begins shift
[1518-04-14 00:47] falls asleep
[1518-08-14 00:27] falls asleep
[1518-10-30 00:33] falls asleep
[1518-11-17 00:07] falls asleep
[1518-04-30 00:53] wakes up
[1518-06-01 23:49] Guard #1877 begins shift
[1518-06-07 00:04] Guard #239 begins shift
[1518-11-18 00:14] falls asleep
[1518-04-27 00:54] wakes up
[1518-04-22 00:58] wakes up
[1518-05-08 00:35] falls asleep
[1518-07-18 00:00] Guard #887 begins shift
[1518-04-02 00:41] falls asleep
[1518-09-08 00:59] wakes up
[1518-05-17 00:00] Guard #1913 begins shift
[1518-08-11 00:45] wakes up
[1518-08-21 00:41] falls asleep
[1518-07-08 00:37] falls asleep
[1518-08-11 00:27] falls asleep
[1518-09-16 00:48] wakes up
[1518-08-26 00:03] Guard #877 begins shift
[1518-07-10 00:32] wakes up
[1518-11-20 00:51] wakes up
[1518-06-18 00:02] falls asleep
[1518-11-13 00:59] wakes up
[1518-04-28 00:31] wakes up
[1518-09-01 00:02] falls asleep
[1518-05-01 00:00] Guard #2207 begins shift
[1518-07-27 00:02] Guard #1607 begins shift
[1518-03-11 00:55] wakes up
[1518-04-19 00:39] wakes up
[1518-09-18 00:18] wakes up
[1518-08-07 00:00] Guard #881 begins shift
[1518-08-15 00:39] wakes up
[1518-07-11 00:30] falls asleep
[1518-11-09 23:46] Guard #239 begins shift
[1518-03-30 00:13] falls asleep
[1518-10-31 00:40] wakes up
[1518-04-24 00:50] wakes up
[1518-04-04 00:08] wakes up
[1518-05-19 00:59] wakes up
[1518-10-18 00:48] wakes up
[1518-10-11 00:44] wakes up
[1518-06-29 00:30] falls asleep
[1518-09-12 00:23] falls asleep
[1518-06-18 23:47] Guard #881 begins shift
[1518-04-26 00:00] Guard #881 begins shift
[1518-07-16 23:53] Guard #911 begins shift
[1518-08-30 23:52] Guard #2963 begins shift
[1518-04-02 23:50] Guard #1291 begins shift
[1518-06-23 00:26] wakes up
[1518-05-12 00:00] Guard #331 begins shift
[1518-03-12 00:02] Guard #3539 begins shift
[1518-03-21 00:12] wakes up
[1518-06-07 00:46] falls asleep
[1518-04-22 00:04] Guard #1889 begins shift
[1518-11-13 00:51] wakes up
[1518-10-21 00:57] wakes up
[1518-11-21 00:03] Guard #571 begins shift
[1518-10-28 00:25] falls asleep
[1518-10-04 00:04] Guard #887 begins shift
[1518-07-20 00:48] falls asleep
[1518-10-06 00:53] falls asleep
[1518-09-12 00:36] falls asleep
[1518-05-06 00:33] falls asleep
[1518-03-30 00:07] wakes up
[1518-05-06 00:01] falls asleep
[1518-07-23 00:42] wakes up
[1518-08-06 00:44] wakes up
[1518-08-09 00:38] wakes up
[1518-11-06 00:01] Guard #239 begins shift
[1518-07-21 00:01] Guard #911 begins shift
[1518-03-20 00:19] falls asleep
[1518-05-14 00:00] Guard #1913 begins shift
[1518-03-23 00:57] wakes up
[1518-05-24 00:21] falls asleep
[1518-03-18 00:37] falls asleep
[1518-04-03 23:50] Guard #2441 begins shift
[1518-03-09 00:39] wakes up
[1518-08-15 00:46] falls asleep
[1518-05-07 00:30] wakes up
[1518-03-19 23:59] Guard #1889 begins shift
[1518-06-11 00:37] wakes up
[1518-03-18 00:44] wakes up
[1518-07-25 00:08] falls asleep
[1518-06-26 00:44] falls asleep
[1518-04-10 00:28] wakes up
[1518-11-20 00:40] falls asleep
[1518-05-29 00:50] wakes up
[1518-03-08 23:56] Guard #2963 begins shift
[1518-09-15 00:19] falls asleep
[1518-04-28 00:56] falls asleep
[1518-06-21 00:19] wakes up
[1518-06-18 00:39] wakes up
[1518-07-26 00:48] falls asleep
[1518-07-04 00:07] falls asleep
[1518-03-23 00:53] wakes up
[1518-10-28 00:03] Guard #887 begins shift
[1518-05-15 00:14] falls asleep
[1518-09-29 00:02] Guard #3539 begins shift
[1518-10-27 00:10] wakes up
[1518-10-08 00:54] falls asleep
[1518-10-13 00:00] Guard #239 begins shift
[1518-11-15 00:25] falls asleep
[1518-04-12 00:04] falls asleep
[1518-06-23 00:58] wakes up
[1518-10-21 00:20] falls asleep
[1518-07-30 00:02] Guard #1249 begins shift
[1518-08-25 00:54] wakes up
[1518-06-23 00:49] falls asleep
[1518-09-11 00:21] falls asleep
[1518-05-06 00:41] wakes up
[1518-07-20 00:51] wakes up
[1518-04-01 23:57] Guard #1889 begins shift
[1518-07-30 00:14] falls asleep
[1518-06-01 00:12] falls asleep
[1518-06-29 00:00] Guard #881 begins shift
[1518-08-31 23:54] Guard #971 begins shift
[1518-11-15 00:26] wakes up
[1518-09-06 00:28] wakes up
[1518-08-19 00:53] wakes up
[1518-03-11 00:42] falls asleep
[1518-08-17 00:36] wakes up
[1518-07-26 00:02] Guard #673 begins shift
[1518-05-03 00:55] wakes up
[1518-04-15 23:58] Guard #571 begins shift
[1518-05-05 00:52] falls asleep
[1518-10-15 00:55] wakes up
[1518-11-18 00:54] wakes up
[1518-03-29 23:50] Guard #911 begins shift
[1518-05-13 00:58] wakes up
[1518-09-14 00:34] wakes up
[1518-06-14 00:03] Guard #571 begins shift
[1518-09-21 23:52] Guard #2441 begins shift
[1518-11-12 00:04] Guard #929 begins shift
[1518-05-05 00:00] Guard #2963 begins shift
[1518-09-07 00:30] wakes up
[1518-04-25 00:11] falls asleep
[1518-03-01 00:41] falls asleep
[1518-07-19 23:46] Guard #1249 begins shift
[1518-11-23 00:25] falls asleep
[1518-04-23 00:39] falls asleep
[1518-07-31 00:42] falls asleep
[1518-10-06 00:56] wakes up
[1518-07-14 00:01] Guard #673 begins shift
[1518-10-30 23:59] Guard #239 begins shift
[1518-09-06 23:46] Guard #911 begins shift
[1518-03-04 23:59] Guard #2441 begins shift
[1518-08-28 00:46] wakes up
[1518-05-13 00:52] wakes up
[1518-10-23 00:35] falls asleep
[1518-08-01 00:24] falls asleep
[1518-03-12 00:06] falls asleep
[1518-11-19 00:43] falls asleep
[1518-07-08 23:57] Guard #1291 begins shift
[1518-03-28 00:41] wakes up
[1518-08-13 00:33] wakes up
[1518-10-12 00:31] falls asleep
[1518-06-26 00:00] Guard #971 begins shift
[1518-04-07 00:47] wakes up
[1518-05-04 00:02] falls asleep
[1518-06-26 00:40] wakes up
[1518-09-11 00:00] Guard #1607 begins shift
[1518-07-06 00:32] wakes up
[1518-03-06 00:50] wakes up
[1518-09-27 00:54] falls asleep
[1518-10-15 00:22] falls asleep
[1518-09-20 23:54] Guard #1607 begins shift
[1518-10-27 00:49] falls asleep
[1518-05-12 00:42] falls asleep
[1518-03-23 00:49] wakes up
[1518-05-01 00:57] wakes up
[1518-08-28 23:56] Guard #571 begins shift
[1518-04-23 23:59] Guard #971 begins shift
[1518-08-30 00:53] wakes up
[1518-03-04 00:55] wakes up
[1518-05-29 00:01] Guard #1607 begins shift
[1518-11-13 00:41] falls asleep
[1518-10-16 00:07] falls asleep
[1518-04-09 00:04] Guard #2963 begins shift
[1518-07-22 00:23] falls asleep
[1518-05-19 00:54] falls asleep
[1518-05-09 00:03] falls asleep
[1518-08-03 00:35] wakes up
[1518-04-09 00:56] wakes up
[1518-11-09 00:01] Guard #887 begins shift
[1518-11-01 23:56] Guard #331 begins shift
[1518-06-21 00:07] falls asleep
[1518-07-03 00:57] wakes up
[1518-05-13 00:57] falls asleep
[1518-06-21 23:47] Guard #331 begins shift
[1518-10-18 00:41] falls asleep
[1518-03-23 00:04] Guard #239 begins shift
[1518-04-11 00:15] falls asleep
[1518-07-28 00:46] falls asleep
[1518-03-31 00:43] wakes up
[1518-03-26 00:00] falls asleep
[1518-09-03 00:53] falls asleep
[1518-07-20 00:41] wakes up
[1518-05-08 00:17] falls asleep
[1518-09-28 00:03] Guard #613 begins shift
[1518-04-20 00:56] wakes up
[1518-06-20 00:32] falls asleep
[1518-04-01 00:01] falls asleep
[1518-10-07 00:02] Guard #79 begins shift
[1518-08-23 00:15] falls asleep
[1518-09-04 00:58] wakes up
[1518-11-09 00:09] falls asleep
[1518-07-01 00:58] wakes up
[1518-05-30 23:58] Guard #1021 begins shift
[1518-03-25 00:00] Guard #2963 begins shift
[1518-08-22 00:38] wakes up
[1518-03-25 00:50] falls asleep
[1518-10-01 00:57] wakes up
[1518-06-28 00:01] Guard #881 begins shift
[1518-05-15 00:01] Guard #1291 begins shift
[1518-08-10 00:04] Guard #1249 begins shift
[1518-11-10 00:04] falls asleep
[1518-07-28 00:47] wakes up
[1518-11-13 00:54] falls asleep
[1518-08-14 00:00] Guard #2963 begins shift
[1518-09-24 23:58] Guard #911 begins shift
[1518-08-09 00:58] wakes up
[1518-10-23 23:59] Guard #673 begins shift
[1518-10-06 00:02] Guard #2207 begins shift
[1518-06-22 00:04] falls asleep
[1518-11-21 00:15] falls asleep
[1518-07-04 23:58] Guard #1889 begins shift
[1518-05-05 00:34] wakes up
[1518-05-28 00:26] falls asleep
[1518-07-15 00:31] wakes up
[1518-08-20 00:33] falls asleep
[1518-11-07 00:00] Guard #1249 begins shift
[1518-03-25 23:53] Guard #1021 begins shift
[1518-05-11 00:35] falls asleep
[1518-06-14 00:54] falls asleep
[1518-07-23 00:59] wakes up
[1518-07-02 00:34] wakes up
[1518-03-15 00:39] falls asleep
[1518-06-04 23:51] Guard #1913 begins shift
[1518-05-14 00:53] falls asleep
[1518-08-14 00:58] wakes up
[1518-06-07 00:34] wakes up
[1518-03-05 00:39] falls asleep
[1518-03-17 00:34] falls asleep
[1518-04-30 00:49] wakes up
[1518-07-02 00:17] falls asleep
[1518-05-13 00:40] wakes up
[1518-11-01 00:02] falls asleep
[1518-05-18 00:38] wakes up
[1518-11-15 23:58] Guard #971 begins shift
[1518-09-05 00:53] wakes up
[1518-06-24 00:30] falls asleep
[1518-06-07 00:58] wakes up
[1518-11-03 23:57] Guard #613 begins shift
[1518-10-25 00:47] wakes up
[1518-03-27 00:26] falls asleep
[1518-04-25 00:50] falls asleep
[1518-03-03 23:49] Guard #571 begins shift
[1518-05-16 00:14] falls asleep
[1518-08-13 00:41] wakes up
[1518-08-01 23:57] Guard #613 begins shift
[1518-09-23 00:20] wakes up
[1518-10-27 00:02] falls asleep
[1518-07-02 23:56] Guard #911 begins shift
[1518-10-25 00:04] falls asleep
[1518-04-11 23:46] Guard #911 begins shift
[1518-07-26 00:51] wakes up
[1518-05-01 00:20] falls asleep
[1518-05-22 00:49] wakes up
[1518-06-06 00:31] wakes up
[1518-03-04 00:53] falls asleep
[1518-10-05 00:51] wakes up
[1518-07-11 00:45] wakes up
[1518-06-07 00:52] wakes up
[1518-04-15 00:40] falls asleep
[1518-11-14 00:57] wakes up
[1518-04-04 00:58] wakes up
[1518-05-23 00:09] falls asleep
[1518-09-13 00:53] wakes up
[1518-07-21 00:51] wakes up
[1518-04-05 00:25] wakes up
[1518-04-26 00:50] wakes up
[1518-08-21 00:02] Guard #1889 begins shift
[1518-05-13 00:03] Guard #1249 begins shift
[1518-08-22 23:57] Guard #1913 begins shift
[1518-08-24 00:54] wakes up
[1518-10-26 00:03] Guard #1913 begins shift
[1518-03-26 00:58] wakes up
[1518-11-08 00:40] falls asleep
[1518-07-17 00:02] falls asleep
[1518-03-30 00:31] falls asleep
[1518-08-12 00:14] falls asleep
[1518-05-31 00:38] wakes up
[1518-09-11 00:39] falls asleep
[1518-05-28 00:49] wakes up
[1518-05-31 00:32] falls asleep
[1518-09-25 23:56] Guard #877 begins shift
[1518-09-10 00:44] falls asleep
[1518-10-06 00:15] falls asleep
[1518-03-23 00:52] falls asleep
[1518-06-07 00:29] falls asleep
[1518-03-21 00:30] falls asleep
[1518-07-28 00:01] Guard #1291 begins shift
[1518-10-13 23:56] Guard #929 begins shift
[1518-11-22 00:28] falls asleep
[1518-03-14 23:59] Guard #613 begins shift
[1518-03-03 00:53] falls asleep
[1518-08-03 00:02] falls asleep
[1518-03-06 23:56] Guard #2207 begins shift
[1518-04-22 00:24] falls asleep
[1518-06-08 00:31] falls asleep
[1518-05-23 00:23] wakes up
[1518-07-08 00:01] Guard #1249 begins shift
[1518-03-15 00:59] wakes up
[1518-06-07 00:56] falls asleep
[1518-09-29 00:57] wakes up
[1518-05-05 00:13] falls asleep
[1518-06-09 00:56] wakes up
[1518-08-16 00:00] Guard #613 begins shift
[1518-11-09 00:58] wakes up
[1518-09-12 00:31] wakes up
[1518-09-07 00:36] falls asleep
[1518-06-22 00:46] falls asleep
[1518-08-05 00:01] Guard #2441 begins shift
[1518-04-01 00:42] wakes up
[1518-06-28 00:53] wakes up
[1518-10-23 00:02] Guard #887 begins shift
[1518-08-07 00:57] wakes up
[1518-06-22 00:26] wakes up
[1518-04-21 00:53] falls asleep
[1518-09-19 23:56] Guard #887 begins shift
[1518-11-09 00:50] falls asleep
[1518-11-06 00:44] wakes up
[1518-07-27 00:32] falls asleep
[1518-10-04 23:49] Guard #1249 begins shift
[1518-06-02 00:36] falls asleep
[1518-09-10 00:00] Guard #613 begins shift
[1518-07-02 00:54] wakes up
[1518-09-05 00:00] Guard #2441 begins shift
[1518-09-07 00:57] wakes up
[1518-08-27 00:25] falls asleep
[1518-08-08 00:04] falls asleep
[1518-04-23 00:18] wakes up
[1518-04-18 00:18] falls asleep
[1518-06-08 00:52] wakes up
[1518-05-23 23:56] Guard #911 begins shift
[1518-03-23 23:54] Guard #1889 begins shift
[1518-03-14 00:48] wakes up
[1518-03-14 00:28] falls asleep
[1518-11-03 00:02] Guard #1877 begins shift
[1518-09-07 00:46] falls asleep
[1518-08-02 23:49] Guard #881 begins shift
[1518-04-03 00:04] falls asleep
[1518-03-15 00:51] wakes up
[1518-06-29 00:48] wakes up
[1518-04-17 00:54] wakes up
[1518-11-22 00:57] wakes up
[1518-04-07 00:46] falls asleep
[1518-09-09 00:00] Guard #1607 begins shift
[1518-08-29 23:53] Guard #2963 begins shift
[1518-08-07 23:47] Guard #239 begins shift
[1518-09-17 00:46] wakes up
[1518-07-05 23:57] Guard #1877 begins shift
[1518-09-03 00:43] wakes up
[1518-03-22 00:00] falls asleep
[1518-11-19 00:50] wakes up
[1518-09-22 00:04] falls asleep
[1518-03-25 00:58] wakes up
[1518-10-09 00:01] falls asleep
[1518-08-14 00:49] falls asleep
[1518-08-28 00:37] falls asleep
[1518-05-11 00:54] falls asleep
[1518-05-25 00:30] wakes up
[1518-03-03 00:50] wakes up
[1518-03-10 00:22] falls asleep
[1518-06-11 00:02] Guard #613 begins shift
[1518-05-26 00:28] falls asleep
[1518-11-10 00:34] wakes up
[1518-09-27 00:03] Guard #881 begins shift
[1518-09-28 00:58] wakes up
[1518-04-26 00:55] falls asleep
[1518-04-14 00:59] wakes up
[1518-03-22 00:55] wakes up
[1518-11-10 00:29] wakes up
[1518-09-19 00:57] wakes up
[1518-03-18 00:00] Guard #1021 begins shift
[1518-10-10 00:40] falls asleep
[1518-05-06 00:10] wakes up
[1518-10-04 00:53] wakes up
[1518-09-25 00:55] wakes up
[1518-05-16 00:59] wakes up
[1518-08-26 23:59] Guard #239 begins shift
[1518-06-02 00:05] wakes up
[1518-09-18 00:57] falls asleep
[1518-03-19 00:58] wakes up
[1518-09-02 00:03] Guard #1607 begins shift
[1518-11-06 00:36] falls asleep
[1518-05-13 00:43] falls asleep
[1518-04-28 00:50] wakes up
[1518-03-24 00:55] wakes up
[1518-06-06 00:45] falls asleep
[1518-11-16 00:07] falls asleep
[1518-06-26 00:07] falls asleep
[1518-03-17 00:57] wakes up
[1518-06-03 00:38] wakes up
[1518-09-16 00:22] falls asleep
[1518-10-23 00:43] wakes up
[1518-06-30 00:03] Guard #2441 begins shift
[1518-05-06 00:49] wakes up
[1518-07-12 00:03] Guard #673 begins shift
[1518-11-16 00:23] wakes up
[1518-08-07 00:49] falls asleep
[1518-03-15 23:57] Guard #1291 begins shift
[1518-11-11 00:48] falls asleep
[1518-10-26 23:50] Guard #1877 begins shift
[1518-09-24 00:52] wakes up
[1518-07-03 00:07] falls asleep
[1518-08-10 00:13] wakes up
[1518-05-08 23:54] Guard #971 begins shift
[1518-08-05 00:38] falls asleep
[1518-04-15 00:59] wakes up
[1518-05-12 00:17] wakes up
[1518-06-17 23:46] Guard #2441 begins shift
[1518-03-21 23:50] Guard #2441 begins shift
[1518-10-28 00:28] wakes up
[1518-07-23 00:08] falls asleep
[1518-03-09 00:23] falls asleep
[1518-06-20 23:57] Guard #887 begins shift
[1518-07-19 00:58] wakes up
[1518-07-09 23:59] Guard #2963 begins shift
[1518-09-27 00:55] wakes up
[1518-08-13 00:40] falls asleep
[1518-11-11 00:23] falls asleep
[1518-04-18 00:46] wakes up
[1518-05-30 00:40] falls asleep
[1518-08-11 00:00] Guard #1889 begins shift
[1518-06-02 00:59] wakes up
[1518-10-24 00:51] falls asleep
[1518-07-08 00:23] wakes up
[1518-07-24 00:49] falls asleep
[1518-03-08 00:00] Guard #971 begins shift
[1518-11-19 00:19] wakes up
[1518-09-11 23:59] Guard #571 begins shift
[1518-10-20 00:01] Guard #911 begins shift
[1518-08-21 00:44] wakes up
[1518-08-25 00:07] falls asleep
[1518-08-18 00:24] wakes up
[1518-07-31 00:56] falls asleep
[1518-05-21 00:18] falls asleep
[1518-09-01 00:51] wakes up
[1518-08-02 00:18] falls asleep
[1518-08-30 00:12] wakes up
[1518-10-24 23:51] Guard #673 begins shift
[1518-03-23 00:56] falls asleep
[1518-08-21 00:56] wakes up
[1518-05-06 00:47] falls asleep
[1518-06-01 00:45] falls asleep
[1518-06-14 00:48] wakes up
[1518-07-28 23:56] Guard #1913 begins shift
[1518-06-01 00:40] wakes up
[1518-08-13 00:32] falls asleep
[1518-08-23 23:53] Guard #2441 begins shift
[1518-09-30 00:17] falls asleep
[1518-08-22 00:55] falls asleep
[1518-04-09 00:08] falls asleep
[1518-04-03 00:14] wakes up
[1518-07-18 00:47] wakes up
[1518-07-23 00:52] falls asleep
[1518-11-17 23:50] Guard #1021 begins shift
[1518-09-29 00:52] falls asleep
[1518-10-17 00:48] wakes up
[1518-03-10 00:02] Guard #971 begins shift
[1518-11-16 00:56] wakes up
[1518-10-27 00:54] wakes up
[1518-04-29 00:03] Guard #2963 begins shift
[1518-10-22 00:05] falls asleep
[1518-10-13 00:33] falls asleep
[1518-03-21 00:05] falls asleep
[1518-03-19 00:46] falls asleep
[1518-06-14 00:46] falls asleep
[1518-07-22 23:57] Guard #1249 begins shift
[1518-06-06 00:55] wakes up
[1518-10-21 00:00] Guard #1607 begins shift
[1518-08-23 00:36] wakes up
[1518-08-18 00:00] Guard #2963 begins shift
[1518-11-09 00:17] wakes up
[1518-06-27 00:35] falls asleep
[1518-08-06 00:32] falls asleep
[1518-06-23 00:57] falls asleep
[1518-04-17 23:56] Guard #3539 begins shift
[1518-03-19 00:50] wakes up
[1518-04-15 00:50] wakes up
[1518-06-06 00:22] falls asleep
[1518-05-20 00:44] wakes up
[1518-05-05 00:57] wakes up
[1518-09-23 00:00] Guard #1877 begins shift
[1518-04-13 23:58] Guard #571 begins shift
[1518-07-06 23:57] Guard #1021 begins shift
[1518-03-30 00:02] falls asleep
[1518-10-08 23:50] Guard #881 begins shift
[1518-03-06 00:01] Guard #1889 begins shift
[1518-11-13 00:08] falls asleep
[1518-07-14 00:49] wakes up
[1518-05-21 00:48] wakes up
[1518-04-26 23:56] Guard #2441 begins shift
[1518-10-06 00:39] falls asleep
[1518-09-18 00:59] wakes up
[1518-05-07 00:06] wakes up
[1518-10-12 00:56] wakes up
[1518-05-22 00:38] falls asleep
[1518-11-04 00:45] wakes up
[1518-03-12 00:59] wakes up
[1518-06-21 00:56] wakes up
[1518-04-15 00:00] Guard #1607 begins shift
[1518-04-08 00:20] wakes up
[1518-09-06 00:26] falls asleep
[1518-03-07 00:59] wakes up
[1518-11-18 00:02] falls asleep
[1518-04-08 00:02] Guard #881 begins shift
[1518-07-13 00:31] wakes up
[1518-11-18 00:11] wakes up
[1518-09-16 00:02] falls asleep
[1518-10-03 00:00] Guard #1889 begins shift
[1518-04-06 00:58] wakes up
[1518-08-02 00:59] wakes up
[1518-08-24 00:01] falls asleep
[1518-07-23 23:59] Guard #887 begins shift
[1518-11-04 23:59] Guard #929 begins shift
[1518-05-01 00:37] wakes up
[1518-03-13 00:01] Guard #1889 begins shift
[1518-09-15 23:51] Guard #881 begins shift
[1518-05-11 00:04] Guard #239 begins shift
[1518-03-05 00:20] falls asleep
[1518-06-20 00:43] falls asleep
[1518-10-05 00:14] wakes up
[1518-09-30 00:01] Guard #571 begins shift
[1518-08-17 00:55] wakes up
[1518-07-07 00:54] wakes up
[1518-10-31 00:26] falls asleep
[1518-06-30 00:28] falls asleep
[1518-08-14 23:58] Guard #1913 begins shift
[1518-05-08 00:37] wakes up
[1518-06-23 00:24] falls asleep
[1518-10-24 00:54] wakes up
[1518-05-25 00:05] falls asleep
[1518-04-01 00:29] wakes up
[1518-08-16 00:57] wakes up
[1518-04-27 23:58] Guard #1249 begins shift
[1518-05-03 00:02] Guard #1889 begins shift
[1518-07-04 00:00] Guard #239 begins shift
[1518-11-21 00:20] wakes up
[1518-09-11 00:26] wakes up
[1518-04-01 00:38] falls asleep
[1518-07-12 00:34] falls asleep
[1518-11-21 23:58] Guard #887 begins shift
[1518-06-29 00:23] wakes up
[1518-11-21 00:35] falls asleep
[1518-05-20 00:01] Guard #887 begins shift
[1518-03-02 00:51] wakes up
[1518-05-05 23:47] Guard #2207 begins shift
[1518-07-23 00:40] falls asleep
[1518-10-29 00:37] falls asleep
[1518-07-25 00:02] Guard #1249 begins shift
[1518-06-17 00:51] wakes up
[1518-10-10 00:00] Guard #1607 begins shift
[1518-05-20 00:10] falls asleep
[1518-11-10 00:32] falls asleep
[1518-09-14 00:31] falls asleep
[1518-03-13 00:45] wakes up
[1518-10-12 00:03] Guard #571 begins shift
[1518-03-06 00:14] falls asleep
[1518-06-21 00:45] falls asleep
[1518-07-30 00:51] wakes up
[1518-04-02 00:57] wakes up
[1518-04-19 00:27] falls asleep
[1518-05-08 00:03] Guard #331 begins shift
[1518-04-11 00:37] falls asleep
[1518-11-16 00:55] falls asleep
[1518-06-19 00:00] falls asleep
[1518-04-18 23:50] Guard #1877 begins shift
[1518-09-20 00:21] falls asleep
[1518-09-28 00:14] falls asleep
[1518-11-07 23:58] Guard #911 begins shift
[1518-08-22 00:59] wakes up
[1518-04-28 00:58] wakes up
[1518-05-15 00:46] wakes up
[1518-03-24 00:03] falls asleep
[1518-04-25 00:37] wakes up
[1518-03-16 00:19] wakes up
[1518-06-05 00:05] falls asleep
[1518-09-24 00:03] Guard #887 begins shift
[1518-07-13 00:22] falls asleep
[1518-11-02 00:47] wakes up
[1518-04-14 00:20] falls asleep
[1518-09-17 00:28] falls asleep
[1518-08-28 00:04] Guard #971 begins shift
[1518-03-02 00:14] falls asleep
[1518-07-25 00:45] wakes up
[1518-06-01 00:48] wakes up
[1518-07-08 00:21] falls asleep
[1518-03-31 00:03] falls asleep
[1518-08-29 00:43] wakes up
[1518-08-14 00:39] wakes up
[1518-08-17 00:10] falls asleep
[1518-09-04 00:04] Guard #571 begins shift
[1518-08-18 00:07] falls asleep
[1518-03-23 00:36] wakes up
[1518-10-29 00:44] wakes up
[1518-03-19 00:53] falls asleep
[1518-07-07 00:19] falls asleep
[1518-03-27 00:51] wakes up
[1518-09-20 00:58] wakes up
[1518-10-29 00:02] Guard #1607 begins shift
[1518-10-19 00:01] Guard #3539 begins shift
[1518-03-19 00:40] wakes up
[1518-09-06 00:04] Guard #1877 begins shift
[1518-06-08 00:03] Guard #881 begins shift
[1518-06-11 00:21] falls asleep
[1518-06-28 00:19] falls asleep
[1518-04-12 00:50] falls asleep
[1518-06-15 00:50] wakes up
[1518-06-13 00:57] wakes up
[1518-05-27 00:39] wakes up
[1518-03-30 00:58] wakes up
[1518-04-29 00:13] falls asleep
[1518-05-02 00:53] wakes up
[1518-10-08 00:35] wakes up
[1518-06-25 00:00] falls asleep
[1518-08-15 00:49] wakes up
[1518-10-30 00:00] Guard #3539 begins shift
[1518-03-20 23:48] Guard #2963 begins shift
[1518-06-09 00:41] falls asleep
[1518-10-01 23:58] Guard #79 begins shift
[1518-04-25 00:02] Guard #2207 begins shift
[1518-05-09 23:57] Guard #929 begins shift
[1518-08-17 00:44] falls asleep
[1518-09-21 00:06] wakes up
[1518-07-08 00:44] wakes up
[1518-06-20 00:37] wakes up
[1518-05-02 00:14] falls asleep
[1518-09-07 00:43] wakes up
[1518-11-16 23:56] Guard #1291 begins shift
[1518-10-17 00:02] falls asleep
[1518-06-05 00:17] wakes up
[1518-03-18 00:15] falls asleep
[1518-11-20 00:04] Guard #1249 begins shift
[1518-05-17 00:34] wakes up
[1518-04-22 23:50] Guard #881 begins shift
[1518-09-02 00:09] falls asleep
[1518-05-19 00:44] wakes up
[1518-03-05 00:50] wakes up
[1518-10-19 00:29] wakes up
[1518-04-12 00:31] wakes up
[1518-05-30 00:48] wakes up
[1518-03-19 00:07] falls asleep
[1518-08-01 00:01] Guard #673 begins shift
[1518-06-26 23:58] Guard #331 begins shift
[1518-08-07 00:21] falls asleep
[1518-07-29 00:33] falls asleep
[1518-09-14 00:50] falls asleep
[1518-03-29 00:45] wakes up
[1518-04-29 23:59] Guard #571 begins shift
[1518-11-14 00:27] falls asleep
[1518-08-31 00:03] falls asleep
[1518-09-03 00:54] wakes up
[1518-06-06 00:03] Guard #1021 begins shift
[1518-04-19 00:10] wakes up
[1518-06-20 00:03] Guard #239 begins shift
[1518-06-29 00:12] falls asleep
[1518-05-24 00:54] wakes up
[1518-05-27 00:00] Guard #2963 begins shift
[1518-07-05 00:47] falls asleep
[1518-06-15 00:04] Guard #239 begins shift
[1518-10-10 00:57] wakes up
[1518-05-27 00:12] falls asleep
[1518-03-07 00:18] falls asleep
[1518-03-30 00:22] wakes up
[1518-08-17 00:22] wakes up
[1518-03-16 00:43] wakes up
[1518-09-09 00:14] falls asleep
[1518-04-11 00:04] Guard #2207 begins shift
[1518-08-08 00:34] wakes up
[1518-11-14 00:50] falls asleep
[1518-10-09 00:54] wakes up
[1518-10-03 00:41] falls asleep
[1518-04-21 00:04] Guard #911 begins shift
[1518-07-31 00:58] wakes up
[1518-03-05 00:31] wakes up
[1518-10-22 00:45] wakes up
[1518-07-11 00:19] wakes up
[1518-11-23 00:39] wakes up
[1518-06-30 00:44] wakes up
[1518-11-11 00:05] wakes up
[1518-05-19 00:00] Guard #571 begins shift
[1518-09-07 23:58] Guard #571 begins shift
[1518-11-19 00:13] falls asleep
[1518-03-18 00:34] wakes up
[1518-08-05 00:51] wakes up
[1518-09-24 00:09] falls asleep
[1518-10-18 00:00] Guard #1607 begins shift
[1518-05-17 23:58] Guard #1021 begins shift
[1518-09-19 00:26] falls asleep
[1518-03-26 00:37] wakes up
[1518-07-23 00:45] falls asleep
[1518-05-01 23:56] Guard #887 begins shift
[1518-07-15 23:59] Guard #929 begins shift
[1518-11-03 00:11] falls asleep
[1518-10-12 00:42] wakes up
[1518-04-02 00:27] falls asleep
[1518-04-20 00:37] wakes up
[1518-06-16 00:37] falls asleep
[1518-09-15 00:43] wakes up
[1518-03-17 00:02] Guard #239 begins shift
[1518-08-31 00:23] wakes up
[1518-09-11 00:51] wakes up
[1518-07-19 00:56] falls asleep
[1518-03-27 00:04] Guard #2441 begins shift
[1518-04-29 00:54] wakes up
[1518-08-12 00:33] falls asleep
[1518-10-16 23:46] Guard #911 begins shift
[1518-07-21 00:14] falls asleep
[1518-06-16 23:56] Guard #1913 begins shift
[1518-05-31 00:25] wakes up
[1518-06-09 23:57] Guard #2441 begins shift
[1518-05-23 00:30] falls asleep
[1518-04-16 00:06] falls asleep
[1518-07-12 00:44] wakes up
[1518-09-27 00:34] wakes up
[1518-06-24 00:01] Guard #911 begins shift
[1518-08-13 00:47] falls asleep
[1518-07-09 00:11] falls asleep
[1518-03-28 00:00] Guard #1249 begins shift
[1518-05-12 00:15] falls asleep
[1518-10-20 00:59] wakes up
[1518-09-13 00:03] Guard #331 begins shift
[1518-04-14 00:44] wakes up
[1518-04-17 00:01] falls asleep
[1518-11-02 00:38] falls asleep
[1518-03-26 00:57] falls asleep
[1518-07-17 00:51] wakes up
[1518-03-01 00:54] wakes up
[1518-07-02 00:03] Guard #571 begins shift
[1518-04-28 00:35] falls asleep
[1518-03-12 00:56] falls asleep
[1518-08-19 00:42] falls asleep
[1518-09-13 00:34] falls asleep
[1518-09-02 00:44] wakes up
[1518-07-21 23:59] Guard #2207 begins shift
[1518-08-07 00:46] wakes up
[1518-07-11 00:00] falls asleep
[1518-10-16 00:57] wakes up
[1518-08-09 00:02] Guard #2963 begins shift
[1518-11-12 23:56] Guard #1889 begins shift
[1518-03-19 00:00] Guard #673 begins shift
[1518-09-03 00:13] falls asleep
[1518-07-22 00:44] wakes up
[1518-10-05 00:37] falls asleep
[1518-07-06 00:44] wakes up
[1518-09-12 00:53] wakes up
[1518-06-20 00:56] wakes up
[1518-08-29 00:27] falls asleep
[1518-09-01 00:32] wakes up
[1518-06-05 00:55] wakes up
[1518-10-05 00:00] falls asleep
[1518-06-13 00:26] falls asleep
[1518-05-31 00:22] falls asleep
[1518-06-19 00:58] wakes up
[1518-07-23 00:49] wakes up
[1518-04-09 23:59] Guard #571 begins shift
[1518-07-09 00:50] wakes up
[1518-07-06 00:28] falls asleep
[1518-10-14 23:58] Guard #881 begins shift
[1518-09-30 23:56] Guard #1889 begins shift
[1518-03-31 23:53] Guard #1249 begins shift
[1518-10-06 00:35] wakes up
[1518-08-13 00:55] wakes up
[1518-04-25 00:58] wakes up
[1518-03-16 00:12] falls asleep
[1518-04-30 00:52] falls asleep
[1518-05-14 00:45] wakes up
[1518-03-28 23:58] Guard #887 begins shift
[1518-07-07 00:22] wakes up
[1518-07-29 00:52] wakes up
[1518-06-25 00:50] wakes up
[1518-05-11 00:06] falls asleep
[1518-03-28 00:33] falls asleep
[1518-05-22 23:56] Guard #2441 begins shift
[1518-08-09 00:52] falls asleep
[1518-02-28 23:56] Guard #887 begins shift
[1518-10-11 00:27] falls asleep
[1518-05-07 00:24] falls asleep
[1518-09-17 23:59] Guard #1877 begins shift
[1518-05-06 23:53] Guard #1291 begins shift
[1518-09-27 00:21] falls asleep
[1518-11-17 00:53] falls asleep
[1518-11-11 00:58] wakes up
[1518-11-21 00:55] wakes up
[1518-06-09 00:01] Guard #1877 begins shift
[1518-03-02 23:56] Guard #2441 begins shift
[1518-08-22 00:33] falls asleep
[1518-04-19 00:01] falls asleep
[1518-04-11 00:24] wakes up
[1518-08-16 00:34] falls asleep
[1518-11-07 00:37] wakes up
[1518-08-12 00:27] wakes up
[1518-06-01 00:54] wakes up
[1518-05-30 00:53] falls asleep
[1518-08-05 23:58] Guard #2441 begins shift
[1518-06-17 00:29] falls asleep
[1518-03-08 00:53] wakes up
[1518-10-01 00:34] falls asleep
[1518-08-20 00:52] wakes up
[1518-08-30 00:52] falls asleep
[1518-11-11 00:38] wakes up
[1518-10-13 00:50] wakes up
[1518-05-08 00:25] wakes up
[1518-06-16 00:55] wakes up
[1518-08-17 00:31] falls asleep
[1518-07-06 00:41] falls asleep
[1518-04-02 00:29] wakes up
[1518-04-26 00:26] falls asleep
[1518-05-11 00:25] wakes up
[1518-04-07 00:01] Guard #571 begins shift
[1518-05-16 00:01] Guard #239 begins shift
[1518-07-22 00:47] falls asleep
[1518-04-20 00:04] Guard #2963 begins shift
[1518-04-24 00:59] wakes up
[1518-05-07 00:01] falls asleep
[1518-11-04 00:30] falls asleep
[1518-10-15 23:57] Guard #1877 begins shift
[1518-06-04 00:01] Guard #79 begins shift
[1518-04-24 00:56] falls asleep
[1518-06-01 00:01] Guard #1877 begins shift
[1518-04-04 00:27] falls asleep
[1518-09-23 00:16] falls asleep
[1518-03-04 00:42] wakes up
[1518-08-22 00:50] wakes up
[1518-10-04 00:59] wakes up
[1518-06-24 00:50] wakes up
[1518-09-10 00:47] wakes up
[1518-06-03 00:37] falls asleep
[1518-11-17 00:57] wakes up
[1518-07-19 00:03] Guard #1249 begins shift
[1518-07-24 00:58] wakes up
[1518-03-13 00:44] falls asleep
[1518-04-12 00:52] wakes up
[1518-04-08 00:48] wakes up
[1518-08-30 00:03] falls asleep
[1518-06-14 00:57] wakes up
[1518-11-17 00:13] wakes up
[1518-07-27 00:44] wakes up
[1518-03-03 00:48] falls asleep
[1518-10-19 00:40] falls asleep
[1518-09-13 23:56] Guard #1291 begins shift
[1518-09-04 00:28] falls asleep
[1518-06-24 23:47] Guard #1913 begins shift
[1518-07-04 00:45] wakes up
[1518-08-09 00:35] falls asleep
[1518-07-14 00:20] falls asleep
[1518-03-14 00:04] Guard #1889 begins shift
[1518-11-18 23:57] Guard #1607 begins shift
[1518-03-24 00:50] falls asleep
[1518-10-08 00:30] falls asleep
[1518-09-30 00:55] wakes up
[1518-06-01 00:51] falls asleep
[1518-06-13 00:32] wakes up
[1518-03-08 00:29] falls asleep
[1518-10-30 00:56] wakes up
[1518-09-21 00:03] falls asleep
[1518-04-21 00:29] wakes up
[1518-03-06 00:40] wakes up
[1518-05-03 23:52] Guard #1877 begins shift
[1518-10-24 00:35] falls asleep
[1518-09-20 00:56] falls asleep
[1518-06-10 00:32] falls asleep
[1518-08-15 00:16] falls asleep
[1518-05-30 00:57] wakes up
[1518-10-26 00:07] falls asleep
[1518-08-05 00:06] falls asleep
[1518-05-25 23:57] Guard #2207 begins shift
[1518-08-19 00:02] Guard #1607 begins shift
[1518-03-12 00:09] wakes up
[1518-04-16 00:38] wakes up
[1518-04-28 00:21] falls asleep
[1518-04-25 00:42] falls asleep
[1518-11-07 00:15] falls asleep
[1518-05-28 00:00] Guard #911 begins shift
[1518-05-17 00:16] falls asleep
[1518-03-23 00:39] falls asleep
[1518-03-04 00:04] falls asleep
[1518-06-11 23:58] Guard #929 begins shift
[1518-09-18 23:58] Guard #1021 begins shift
[1518-07-14 23:58] Guard #239 begins shift
[1518-08-22 00:46] falls asleep
[1518-03-23 00:31] falls asleep
[1518-05-09 00:07] wakes up
[1518-03-12 00:40] falls asleep
[1518-05-23 00:57] wakes up
[1518-04-24 00:16] falls asleep
[1518-05-12 00:56] wakes up
[1518-04-04 00:01] falls asleep
[1518-05-20 23:57] Guard #2207 begins shift
[1518-05-19 00:20] falls asleep
[1518-04-27 00:14] falls asleep
[1518-11-14 00:32] wakes up
[1518-08-11 23:59] Guard #1607 begins shift
[1518-04-11 00:58] wakes up
[1518-07-31 00:51] wakes up
[1518-05-21 23:58] Guard #971 begins shift
[1518-10-24 00:46] wakes up
[1518-08-21 23:56] Guard #239 begins shift
[1518-10-31 23:47] Guard #2963 begins shift
[1518-03-11 00:00] Guard #571 begins shift
[1518-04-20 00:53] falls asleep
[1518-10-08 00:58] wakes up
[1518-03-15 00:55] falls asleep
[1518-04-08 00:34] falls asleep
[1518-06-10 00:40] wakes up
[1518-08-13 00:00] Guard #3539 begins shift
[1518-04-10 00:21] falls asleep
[1518-06-26 00:49] wakes up
[1518-09-05 00:39] falls asleep
[1518-05-04 00:28] wakes up
[1518-11-11 00:04] falls asleep
[1518-03-02 00:02] Guard #2441 begins shift
[1518-10-20 00:28] falls asleep
[1518-05-24 23:47] Guard #2963 begins shift
[1518-09-15 00:00] Guard #1607 begins shift
[1518-07-30 23:58] Guard #1291 begins shift
[1518-11-01 00:08] wakes up
[1518-05-29 23:56] Guard #331 begins shift
[1518-10-04 00:56] falls asleep
[1518-04-26 00:56] wakes up
[1518-06-27 00:53] wakes up
[1518-10-10 23:56] Guard #1021 begins shift
[1518-05-11 00:58] wakes up
[1518-03-10 00:56] wakes up
[1518-08-17 00:01] Guard #1021 begins shift
[1518-03-16 00:39] falls asleep
"""

testdata = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""

testdata_unsorted = """
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""

from datetime import datetime
from collections import Counter 

def mark_asleep(counter, start_hours, start_minutes, end_hours, end_minutes):
  while(True):
    key = "%d:%d" % (start_hours, start_minutes)
    counter[key] += 1
    start_minutes += 1
    if start_minutes >= 60:
      start_minutes = 0
      start_hours += 1
    if start_hours >= 24:
      start_hours = 0
    if start_hours == end_hours and start_minutes == end_minutes: break


def day4_2(input):
  values = {}
  timestamps = {}
  delta = datetime.now()
  delta = delta.replace(year=1500)
  for line in input.split("\n"):
    if len(line.strip()) == 0:
      continue
    sections = line.split("]")
    dateandtime = sections[0][1:]
    message = sections[1].strip()
    timestamp = datetime.strptime(dateandtime, "%Y-%m-%d %H:%M")
    
    seconds_since = (timestamp - delta).total_seconds()
    values[seconds_since]=message
    timestamps[seconds_since]=timestamp
    
  dict_keys = sorted(values.keys())  
  guard = None
  start_time = None
  asleep_times = Counter()
  most_asleep = {}
  for key in dict_keys:
    value = values[key]  
    if value.find("#") > 0:
      value = value[7:]
      guard = value[:value.find(" ")]
      print ("Guard is %s" % guard)
      try:
        minute_tracker = most_asleep[guard]
      except KeyError:
        most_asleep[guard] = Counter()
    elif value == "falls asleep":
      start_time = key
      print ("Asleep")
    elif value == "wakes up":
      end_time = key
      seconds_asleep = end_time - start_time
      minutes_asleep = int(seconds_asleep / 60)      
      asleep_times[guard] += minutes_asleep
      start_hours = timestamps[start_time].hour
      start_minutes = timestamps[start_time].minute
      end_hours = timestamps[end_time].hour
      end_minutes = timestamps[end_time].minute
      mark_asleep(most_asleep[guard], start_hours, start_minutes, end_hours, end_minutes)
      print ("Awake after %d minutes" % minutes_asleep)
      print ("Total is now %d minutes" % asleep_times[guard])
      
  print (asleep_times.most_common())
  most_asleep_guard = int(asleep_times.most_common()[0][0])
  most_asleep_minutes = asleep_times.most_common()[0][1]
  most_asleep_count = 0
  guard_to_choose = None
  for guard in most_asleep.keys():
    print(guard)
    print("***")
    if len(most_asleep[guard].most_common()) == 0:
      continue
    
    print("***")
    most_common_for_this_guard = most_asleep[guard].most_common()[0][0]
    print(most_common_for_this_guard)
    times_for_this_guard = most_asleep[guard].most_common()[0][1]
    print (times_for_this_guard)
    if times_for_this_guard > most_asleep_count:
      most_asleep_count = times_for_this_guard
      guard_to_choose = guard
  most_asleep_minute = most_asleep[guard_to_choose].most_common()[0][0]
  time_struct = most_asleep_minute.split(":")
  minute_number = int(time_struct[0]) * 60 + int(time_struct[1])
   
  calculated_value = int(guard_to_choose) * minute_number
  print(calculated_value)
  return calculated_value

assert(day4_2(testdata_unsorted) == 4455)
print (day4_2(input))