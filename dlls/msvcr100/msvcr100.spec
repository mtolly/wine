# MS VC++2010 runtime library

@ thiscall -arch=win32 ??0?$_SpinWait@$00@details@Concurrency@@QAE@P6AXXZ@Z(ptr ptr) SpinWait_ctor_yield
@ cdecl -arch=win64 ??0?$_SpinWait@$00@details@Concurrency@@QEAA@P6AXXZ@Z(ptr ptr) SpinWait_ctor_yield
@ thiscall -arch=win32 ??0?$_SpinWait@$0A@@details@Concurrency@@QAE@P6AXXZ@Z(ptr ptr) SpinWait_ctor
@ cdecl -arch=win64 ??0?$_SpinWait@$0A@@details@Concurrency@@QEAA@P6AXXZ@Z(ptr ptr) SpinWait_ctor
@ varargs -arch=win32 ??0SchedulerPolicy@Concurrency@@QAA@IZZ(ptr long) SchedulerPolicy_ctor_policies
@ varargs -arch=win64 ??0SchedulerPolicy@Concurrency@@QEAA@_KZZ(ptr long) SchedulerPolicy_ctor_policies
@ thiscall -arch=i386 ??0SchedulerPolicy@Concurrency@@QAE@ABV01@@Z(ptr ptr) SchedulerPolicy_copy_ctor
@ cdecl -arch=win64 ??0SchedulerPolicy@Concurrency@@QEAA@AEBV01@@Z(ptr ptr) SchedulerPolicy_copy_ctor
@ thiscall -arch=i386 ??0SchedulerPolicy@Concurrency@@QAE@XZ(ptr) SchedulerPolicy_ctor
@ cdecl -arch=win64 ??0SchedulerPolicy@Concurrency@@QEAA@XZ(ptr) SchedulerPolicy_ctor
@ thiscall -arch=win32 ??0_NonReentrantBlockingLock@details@Concurrency@@QAE@XZ(ptr) _ReentrantBlockingLock_ctor
@ cdecl -arch=win64 ??0_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ(ptr) _ReentrantBlockingLock_ctor
@ thiscall -arch=win32 ??0_NonReentrantPPLLock@details@Concurrency@@QAE@XZ(ptr) _NonReentrantPPLLock_ctor
@ cdecl -arch=win64 ??0_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ(ptr) _NonReentrantPPLLock_ctor
@ stub -arch=win32 ??0_ReaderWriterLock@details@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0_ReaderWriterLock@details@Concurrency@@QEAA@XZ
@ thiscall -arch=win32 ??0_ReentrantBlockingLock@details@Concurrency@@QAE@XZ(ptr) _ReentrantBlockingLock_ctor
@ cdecl -arch=win64 ??0_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ(ptr) _ReentrantBlockingLock_ctor
@ stub -arch=win32 ??0_ReentrantLock@details@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0_ReentrantLock@details@Concurrency@@QEAA@XZ
@ thiscall -arch=win32 ??0_ReentrantPPLLock@details@Concurrency@@QAE@XZ(ptr) _ReentrantPPLLock_ctor
@ cdecl -arch=win64 ??0_ReentrantPPLLock@details@Concurrency@@QEAA@XZ(ptr) _ReentrantPPLLock_ctor
@ thiscall -arch=win32 ??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QAE@AAV123@@Z(ptr ptr) _NonReentrantPPLLock__Scoped_lock_ctor
@ cdecl -arch=win64 ??0_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z(ptr ptr) _NonReentrantPPLLock__Scoped_lock_ctor
@ thiscall -arch=win32 ??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QAE@AAV123@@Z(ptr ptr) _ReentrantPPLLock__Scoped_lock_ctor
@ cdecl -arch=win64 ??0_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@AEAV123@@Z(ptr ptr) _ReentrantPPLLock__Scoped_lock_ctor
@ stub -arch=win32 ??0_SpinLock@details@Concurrency@@QAE@ACJ@Z
@ stub -arch=win64 ??0_SpinLock@details@Concurrency@@QEAA@AECJ@Z
@ stub -arch=win32 ??0_TaskCollection@details@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0_TaskCollection@details@Concurrency@@QEAA@XZ
@ thiscall -arch=win32 ??0_Timer@details@Concurrency@@IAE@I_N@Z(ptr long long) _Timer_ctor
@ cdecl -arch=win64 ??0_Timer@details@Concurrency@@IEAA@I_N@Z(ptr long long) _Timer_ctor
@ thiscall -arch=i386 ??0__non_rtti_object@std@@QAE@ABV01@@Z(ptr ptr) __non_rtti_object_copy_ctor
@ cdecl -arch=win64 ??0__non_rtti_object@std@@QEAA@AEBV01@@Z(ptr ptr) __non_rtti_object_copy_ctor
@ thiscall -arch=i386 ??0__non_rtti_object@std@@QAE@PBD@Z(ptr ptr) __non_rtti_object_ctor
@ cdecl -arch=win64 ??0__non_rtti_object@std@@QEAA@PEBD@Z(ptr ptr) __non_rtti_object_ctor
@ thiscall -arch=i386 ??0bad_cast@std@@AAE@PBQBD@Z(ptr ptr) bad_cast_ctor
@ cdecl -arch=win64 ??0bad_cast@std@@AEAA@PEBQEBD@Z(ptr ptr) bad_cast_ctor
@ thiscall -arch=i386 ??0bad_cast@std@@QAE@ABV01@@Z(ptr ptr) bad_cast_copy_ctor
@ cdecl -arch=win64 ??0bad_cast@std@@QEAA@AEBV01@@Z(ptr ptr) bad_cast_copy_ctor
@ thiscall -arch=i386 ??0bad_cast@std@@QAE@PBD@Z(ptr str) bad_cast_ctor_charptr
@ cdecl -arch=win64 ??0bad_cast@std@@QEAA@PEBD@Z(ptr str) bad_cast_ctor_charptr
@ stub -arch=win32 ??0bad_target@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0bad_target@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0bad_target@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0bad_target@Concurrency@@QEAA@XZ
@ thiscall -arch=i386 ??0bad_typeid@std@@QAE@ABV01@@Z(ptr ptr) bad_typeid_copy_ctor
@ cdecl -arch=win64 ??0bad_typeid@std@@QEAA@AEBV01@@Z(ptr ptr) bad_typeid_copy_ctor
@ thiscall -arch=i386 ??0bad_typeid@std@@QAE@PBD@Z(ptr str) bad_typeid_ctor
@ cdecl -arch=win64 ??0bad_typeid@std@@QEAA@PEBD@Z(ptr str) bad_typeid_ctor
@ stub -arch=win32 ??0context_self_unblock@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0context_self_unblock@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0context_self_unblock@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0context_self_unblock@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0context_unblock_unbalanced@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0context_unblock_unbalanced@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0context_unblock_unbalanced@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0context_unblock_unbalanced@Concurrency@@QEAA@XZ
@ thiscall -arch=win32 ??0critical_section@Concurrency@@QAE@XZ(ptr) critical_section_ctor
@ cdecl -arch=win64 ??0critical_section@Concurrency@@QEAA@XZ(ptr) critical_section_ctor
@ stub -arch=win32 ??0default_scheduler_exists@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0default_scheduler_exists@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0default_scheduler_exists@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0default_scheduler_exists@Concurrency@@QEAA@XZ
@ thiscall -arch=win32 ??0event@Concurrency@@QAE@XZ(ptr) event_ctor
@ cdecl -arch=win64 ??0event@Concurrency@@QEAA@XZ(ptr) event_ctor
@ thiscall -arch=i386 ??0exception@std@@QAE@ABQBD@Z(ptr ptr) exception_ctor
@ cdecl -arch=win64 ??0exception@std@@QEAA@AEBQEBD@Z(ptr ptr) exception_ctor
@ thiscall -arch=i386 ??0exception@std@@QAE@ABQBDH@Z(ptr ptr long) exception_ctor_noalloc
@ cdecl -arch=win64 ??0exception@std@@QEAA@AEBQEBDH@Z(ptr ptr long) exception_ctor_noalloc
@ thiscall -arch=i386 ??0exception@std@@QAE@ABV01@@Z(ptr ptr) exception_copy_ctor
@ cdecl -arch=win64 ??0exception@std@@QEAA@AEBV01@@Z(ptr ptr) exception_copy_ctor
@ thiscall -arch=i386 ??0exception@std@@QAE@XZ(ptr) exception_default_ctor
@ cdecl -arch=win64 ??0exception@std@@QEAA@XZ(ptr) exception_default_ctor
@ thiscall -arch=i386 ??0improper_lock@Concurrency@@QAE@PBD@Z(ptr str) improper_lock_ctor_str
@ cdecl -arch=win64 ??0improper_lock@Concurrency@@QEAA@PEBD@Z(ptr str) improper_lock_ctor_str
@ thiscall -arch=i386 ??0improper_lock@Concurrency@@QAE@XZ(ptr) improper_lock_ctor
@ cdecl -arch=win64 ??0improper_lock@Concurrency@@QEAA@XZ(ptr) improper_lock_ctor
@ thiscall -arch=i386 ??0improper_scheduler_attach@Concurrency@@QAE@PBD@Z(ptr str) improper_scheduler_attach_ctor_str
@ cdecl -arch=win64 ??0improper_scheduler_attach@Concurrency@@QEAA@PEBD@Z(ptr str) improper_scheduler_attach_ctor_str
@ thiscall -arch=i386 ??0improper_scheduler_attach@Concurrency@@QAE@XZ(ptr) improper_scheduler_attach_ctor
@ cdecl -arch=win64 ??0improper_scheduler_attach@Concurrency@@QEAA@XZ(ptr) improper_scheduler_attach_ctor
@ thiscall -arch=i386 ??0improper_scheduler_detach@Concurrency@@QAE@PBD@Z(ptr str) improper_scheduler_detach_ctor_str
@ cdecl -arch=win64 ??0improper_scheduler_detach@Concurrency@@QEAA@PEBD@Z(ptr str) improper_scheduler_detach_ctor_str
@ thiscall -arch=i386 ??0improper_scheduler_detach@Concurrency@@QAE@XZ(ptr) improper_scheduler_detach_ctor
@ cdecl -arch=win64 ??0improper_scheduler_detach@Concurrency@@QEAA@XZ(ptr) improper_scheduler_detach_ctor
@ stub -arch=win32 ??0improper_scheduler_reference@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0improper_scheduler_reference@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0improper_scheduler_reference@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0improper_scheduler_reference@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0invalid_link_target@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0invalid_link_target@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0invalid_link_target@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0invalid_link_target@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0invalid_multiple_scheduling@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0invalid_multiple_scheduling@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0invalid_multiple_scheduling@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0invalid_multiple_scheduling@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0invalid_operation@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0invalid_operation@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0invalid_operation@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0invalid_operation@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0invalid_oversubscribe_operation@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0invalid_oversubscribe_operation@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0invalid_oversubscribe_operation@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0invalid_oversubscribe_operation@Concurrency@@QEAA@XZ
@ thiscall -arch=i386 ??0invalid_scheduler_policy_key@Concurrency@@QAE@PBD@Z(ptr str) invalid_scheduler_policy_key_ctor_str
@ cdecl -arch=win64 ??0invalid_scheduler_policy_key@Concurrency@@QEAA@PEBD@Z(ptr str) invalid_scheduler_policy_key_ctor_str
@ thiscall -arch=i386 ??0invalid_scheduler_policy_key@Concurrency@@QAE@XZ(ptr) invalid_scheduler_policy_key_ctor
@ cdecl -arch=win64 ??0invalid_scheduler_policy_key@Concurrency@@QEAA@XZ(ptr) invalid_scheduler_policy_key_ctor
@ thiscall -arch=i386 ??0invalid_scheduler_policy_thread_specification@Concurrency@@QAE@PBD@Z(ptr str) invalid_scheduler_policy_thread_specification_ctor_str
@ cdecl -arch=win64 ??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@PEBD@Z(ptr str) invalid_scheduler_policy_thread_specification_ctor_str
@ thiscall -arch=i386 ??0invalid_scheduler_policy_thread_specification@Concurrency@@QAE@XZ(ptr) invalid_scheduler_policy_thread_specification_ctor
@ cdecl -arch=win64 ??0invalid_scheduler_policy_thread_specification@Concurrency@@QEAA@XZ(ptr) invalid_scheduler_policy_thread_specification_ctor
@ thiscall -arch=i386 ??0invalid_scheduler_policy_value@Concurrency@@QAE@PBD@Z(ptr str) invalid_scheduler_policy_value_ctor_str
@ cdecl -arch=win64 ??0invalid_scheduler_policy_value@Concurrency@@QEAA@PEBD@Z(ptr str) invalid_scheduler_policy_value_ctor_str
@ thiscall -arch=i386 ??0invalid_scheduler_policy_value@Concurrency@@QAE@XZ(ptr) invalid_scheduler_policy_value_ctor
@ cdecl -arch=win64 ??0invalid_scheduler_policy_value@Concurrency@@QEAA@XZ(ptr) invalid_scheduler_policy_value_ctor
@ stub -arch=win32 ??0message_not_found@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0message_not_found@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0message_not_found@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0message_not_found@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0missing_wait@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0missing_wait@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0missing_wait@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0missing_wait@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0nested_scheduler_missing_detach@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0nested_scheduler_missing_detach@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0nested_scheduler_missing_detach@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0nested_scheduler_missing_detach@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0operation_timed_out@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0operation_timed_out@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0operation_timed_out@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0operation_timed_out@Concurrency@@QEAA@XZ
@ thiscall -arch=win32 ??0reader_writer_lock@Concurrency@@QAE@XZ(ptr) reader_writer_lock_ctor
@ cdecl -arch=win64 ??0reader_writer_lock@Concurrency@@QEAA@XZ(ptr) reader_writer_lock_ctor
@ stub -arch=win32 ??0scheduler_not_attached@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0scheduler_not_attached@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0scheduler_not_attached@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0scheduler_not_attached@Concurrency@@QEAA@XZ
@ thiscall -arch=i386 ??0scheduler_resource_allocation_error@Concurrency@@QAE@J@Z(ptr long) scheduler_resource_allocation_error_ctor
@ cdecl -arch=win64 ??0scheduler_resource_allocation_error@Concurrency@@QEAA@J@Z(ptr long) scheduler_resource_allocation_error_ctor
@ thiscall -arch=i386 ??0scheduler_resource_allocation_error@Concurrency@@QAE@PBDJ@Z(ptr str long) scheduler_resource_allocation_error_ctor_name
@ cdecl -arch=win64 ??0scheduler_resource_allocation_error@Concurrency@@QEAA@PEBDJ@Z(ptr str long) scheduler_resource_allocation_error_ctor_name
@ thiscall -arch=win32 ??0scoped_lock@critical_section@Concurrency@@QAE@AAV12@@Z(ptr ptr) critical_section_scoped_lock_ctor
@ cdecl -arch=win64 ??0scoped_lock@critical_section@Concurrency@@QEAA@AEAV12@@Z(ptr ptr) critical_section_scoped_lock_ctor
@ thiscall -arch=win32 ??0scoped_lock@reader_writer_lock@Concurrency@@QAE@AAV12@@Z(ptr ptr) reader_writer_lock_scoped_lock_ctor
@ cdecl -arch=win64 ??0scoped_lock@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z(ptr ptr) reader_writer_lock_scoped_lock_ctor
@ thiscall -arch=win32 ??0scoped_lock_read@reader_writer_lock@Concurrency@@QAE@AAV12@@Z(ptr ptr) reader_writer_lock_scoped_lock_read_ctor
@ cdecl -arch=win64 ??0scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@AEAV12@@Z(ptr ptr) reader_writer_lock_scoped_lock_read_ctor
@ stub -arch=win32 ??0task_canceled@details@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0task_canceled@details@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0task_canceled@details@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0task_canceled@details@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??0unsupported_os@Concurrency@@QAE@PBD@Z
@ stub -arch=win64 ??0unsupported_os@Concurrency@@QEAA@PEBD@Z
@ stub -arch=win32 ??0unsupported_os@Concurrency@@QAE@XZ
@ stub -arch=win64 ??0unsupported_os@Concurrency@@QEAA@XZ
@ thiscall -arch=i386 ??1SchedulerPolicy@Concurrency@@QAE@XZ(ptr) SchedulerPolicy_dtor
@ cdecl -arch=win64 ??1SchedulerPolicy@Concurrency@@QEAA@XZ(ptr) SchedulerPolicy_dtor
@ thiscall -arch=win32 ??1_NonReentrantBlockingLock@details@Concurrency@@QAE@XZ(ptr) _ReentrantBlockingLock_dtor
@ cdecl -arch=win64 ??1_NonReentrantBlockingLock@details@Concurrency@@QEAA@XZ(ptr) _ReentrantBlockingLock_dtor
@ thiscall -arch=win32 ??1_ReentrantBlockingLock@details@Concurrency@@QAE@XZ(ptr) _ReentrantBlockingLock_dtor
@ cdecl -arch=win64 ??1_ReentrantBlockingLock@details@Concurrency@@QEAA@XZ(ptr) _ReentrantBlockingLock_dtor
@ thiscall -arch=win32 ??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QAE@XZ(ptr) _NonReentrantPPLLock__Scoped_lock_dtor
@ cdecl -arch=win64 ??1_Scoped_lock@_NonReentrantPPLLock@details@Concurrency@@QEAA@XZ(ptr) _NonReentrantPPLLock__Scoped_lock_dtor
@ thiscall -arch=win32 ??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QAE@XZ(ptr) _ReentrantPPLLock__Scoped_lock_dtor
@ cdecl -arch=win64 ??1_Scoped_lock@_ReentrantPPLLock@details@Concurrency@@QEAA@XZ(ptr) _ReentrantPPLLock__Scoped_lock_dtor
@ stub -arch=win32 ??1_SpinLock@details@Concurrency@@QAE@XZ
@ stub -arch=win64 ??1_SpinLock@details@Concurrency@@QEAA@XZ
@ stub -arch=win32 ??1_TaskCollection@details@Concurrency@@QAE@XZ
@ stub -arch=win64 ??1_TaskCollection@details@Concurrency@@QEAA@XZ
@ thiscall -arch=win32 ??1_Timer@details@Concurrency@@IAE@XZ(ptr) _Timer_dtor
@ cdecl -arch=win64 ??1_Timer@details@Concurrency@@IEAA@XZ(ptr) _Timer_dtor
@ thiscall -arch=i386 ??1__non_rtti_object@std@@UAE@XZ(ptr) __non_rtti_object_dtor
@ cdecl -arch=win64 ??1__non_rtti_object@std@@UEAA@XZ(ptr) __non_rtti_object_dtor
@ thiscall -arch=i386 ??1bad_cast@std@@UAE@XZ(ptr) bad_cast_dtor
@ cdecl -arch=win64 ??1bad_cast@std@@UEAA@XZ(ptr) bad_cast_dtor
@ thiscall -arch=i386 ??1bad_typeid@std@@UAE@XZ(ptr) bad_typeid_dtor
@ cdecl -arch=win64 ??1bad_typeid@std@@UEAA@XZ(ptr) bad_typeid_dtor
@ thiscall -arch=win32 ??1critical_section@Concurrency@@QAE@XZ(ptr) critical_section_dtor
@ cdecl -arch=win64 ??1critical_section@Concurrency@@QEAA@XZ(ptr) critical_section_dtor
@ thiscall -arch=win32 ??1event@Concurrency@@QAE@XZ(ptr) event_dtor
@ cdecl -arch=win64 ??1event@Concurrency@@QEAA@XZ(ptr) event_dtor
@ thiscall -arch=i386 ??1exception@std@@UAE@XZ(ptr) exception_dtor
@ cdecl -arch=win64 ??1exception@std@@UEAA@XZ(ptr) exception_dtor
@ thiscall -arch=win32 ??1reader_writer_lock@Concurrency@@QAE@XZ(ptr) reader_writer_lock_dtor
@ cdecl -arch=win64 ??1reader_writer_lock@Concurrency@@QEAA@XZ(ptr) reader_writer_lock_dtor
@ thiscall -arch=win32 ??1scoped_lock@critical_section@Concurrency@@QAE@XZ(ptr) critical_section_scoped_lock_dtor
@ cdecl -arch=win64 ??1scoped_lock@critical_section@Concurrency@@QEAA@XZ(ptr) critical_section_scoped_lock_dtor
@ thiscall -arch=win32 ??1scoped_lock@reader_writer_lock@Concurrency@@QAE@XZ(ptr) reader_writer_lock_scoped_lock_dtor
@ cdecl -arch=win64 ??1scoped_lock@reader_writer_lock@Concurrency@@QEAA@XZ(ptr) reader_writer_lock_scoped_lock_dtor
@ thiscall -arch=win32 ??1scoped_lock_read@reader_writer_lock@Concurrency@@QAE@XZ(ptr) reader_writer_lock_scoped_lock_read_dtor
@ cdecl -arch=win64 ??1scoped_lock_read@reader_writer_lock@Concurrency@@QEAA@XZ(ptr) reader_writer_lock_scoped_lock_read_dtor
@ cdecl -arch=arm ??1type_info@@UAA@XZ(ptr) type_info_dtor
@ thiscall -arch=i386 ??1type_info@@UAE@XZ(ptr) type_info_dtor
@ cdecl -arch=win64 ??1type_info@@UEAA@XZ(ptr) type_info_dtor
@ cdecl -arch=win32 ??2@YAPAXI@Z(long) operator_new
@ cdecl -arch=win64 ??2@YAPEAX_K@Z(long) operator_new
@ cdecl -arch=win32 ??2@YAPAXIHPBDH@Z(long long str long) operator_new_dbg
@ cdecl -arch=win64 ??2@YAPEAX_KHPEBDH@Z(long long str long) operator_new_dbg
@ cdecl -arch=win32 ??3@YAXPAX@Z(ptr) operator_delete
@ cdecl -arch=win64 ??3@YAXPEAX@Z(ptr) operator_delete
@ stub -arch=win32 ??4?$_SpinWait@$00@details@Concurrency@@QAEAAV012@ABV012@@Z
@ stub -arch=win64 ??4?$_SpinWait@$00@details@Concurrency@@QEAAAEAV012@AEBV012@@Z
@ stub -arch=win32 ??4?$_SpinWait@$0A@@details@Concurrency@@QAEAAV012@ABV012@@Z
@ stub -arch=win64 ??4?$_SpinWait@$0A@@details@Concurrency@@QEAAAEAV012@AEBV012@@Z
@ thiscall -arch=i386 ??4SchedulerPolicy@Concurrency@@QAEAAV01@ABV01@@Z(ptr ptr) SchedulerPolicy_op_assign
@ cdecl -arch=win64 ??4SchedulerPolicy@Concurrency@@QEAAAEAV01@AEBV01@@Z(ptr ptr) SchedulerPolicy_op_assign
@ thiscall -arch=i386 ??4__non_rtti_object@std@@QAEAAV01@ABV01@@Z(ptr ptr) __non_rtti_object_opequals
@ cdecl -arch=win64 ??4__non_rtti_object@std@@QEAAAEAV01@AEBV01@@Z(ptr ptr) __non_rtti_object_opequals
@ thiscall -arch=i386 ??4bad_cast@std@@QAEAAV01@ABV01@@Z(ptr ptr) bad_cast_opequals
@ cdecl -arch=win64 ??4bad_cast@std@@QEAAAEAV01@AEBV01@@Z(ptr ptr) bad_cast_opequals
@ thiscall -arch=i386 ??4bad_typeid@std@@QAEAAV01@ABV01@@Z(ptr ptr) bad_typeid_opequals
@ cdecl -arch=win64 ??4bad_typeid@std@@QEAAAEAV01@AEBV01@@Z(ptr ptr) bad_typeid_opequals
@ thiscall -arch=i386 ??4exception@std@@QAEAAV01@ABV01@@Z(ptr ptr) exception_opequals
@ cdecl -arch=win64 ??4exception@std@@QEAAAEAV01@AEBV01@@Z(ptr ptr) exception_opequals
@ cdecl -arch=arm ??8type_info@@QBA_NABV0@@Z(ptr ptr) type_info_opequals_equals
@ thiscall -arch=i386 ??8type_info@@QBE_NABV0@@Z(ptr ptr) type_info_opequals_equals
@ cdecl -arch=win64 ??8type_info@@QEBA_NAEBV0@@Z(ptr ptr) type_info_opequals_equals
@ cdecl -arch=arm ??9type_info@@QBA_NABV0@@Z(ptr ptr) type_info_opnot_equals
@ thiscall -arch=i386 ??9type_info@@QBE_NABV0@@Z(ptr ptr) type_info_opnot_equals
@ cdecl -arch=win64 ??9type_info@@QEBA_NAEBV0@@Z(ptr ptr) type_info_opnot_equals
@ extern ??_7__non_rtti_object@std@@6B@ __non_rtti_object_vtable
@ extern ??_7bad_cast@std@@6B@ bad_cast_vtable
@ extern ??_7bad_typeid@std@@6B@ bad_typeid_vtable
@ extern ??_7exception@@6B@ exception_old_vtable
@ extern ??_7exception@std@@6B@ exception_vtable
@ thiscall -arch=win32 ??_F?$_SpinWait@$00@details@Concurrency@@QAEXXZ(ptr) SpinWait_dtor
@ cdecl -arch=win64 ??_F?$_SpinWait@$00@details@Concurrency@@QEAAXXZ(ptr) SpinWait_dtor
@ thiscall -arch=win32 ??_F?$_SpinWait@$0A@@details@Concurrency@@QAEXXZ(ptr) SpinWait_dtor
@ cdecl -arch=win64 ??_F?$_SpinWait@$0A@@details@Concurrency@@QEAAXXZ(ptr) SpinWait_dtor
@ thiscall -arch=i386 ??_Fbad_cast@std@@QAEXXZ(ptr) bad_cast_default_ctor
@ cdecl -arch=win64 ??_Fbad_cast@std@@QEAAXXZ(ptr) bad_cast_default_ctor
@ thiscall -arch=i386 ??_Fbad_typeid@std@@QAEXXZ(ptr) bad_typeid_default_ctor
@ cdecl -arch=win64 ??_Fbad_typeid@std@@QEAAXXZ(ptr) bad_typeid_default_ctor
@ cdecl -arch=win32 ??_U@YAPAXI@Z(long) operator_new
@ cdecl -arch=win64 ??_U@YAPEAX_K@Z(long) operator_new
@ cdecl -arch=win32 ??_U@YAPAXIHPBDH@Z(long long str long) operator_new_dbg
@ cdecl -arch=win64 ??_U@YAPEAX_KHPEBDH@Z(long long str long) operator_new_dbg
@ cdecl -arch=win32 ??_V@YAXPAX@Z(ptr) operator_delete
@ cdecl -arch=win64 ??_V@YAXPEAX@Z(ptr) operator_delete
@ cdecl -arch=win32 ?Alloc@Concurrency@@YAPAXI@Z(long) Concurrency_Alloc
@ cdecl -arch=win64 ?Alloc@Concurrency@@YAPEAX_K@Z(long) Concurrency_Alloc
@ cdecl ?Block@Context@Concurrency@@SAXXZ() Context_Block
@ cdecl -arch=win32 ?Create@CurrentScheduler@Concurrency@@SAXABVSchedulerPolicy@2@@Z(ptr) CurrentScheduler_Create
@ cdecl -arch=win64 ?Create@CurrentScheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z(ptr) CurrentScheduler_Create
@ cdecl -arch=win32 ?Create@Scheduler@Concurrency@@SAPAV12@ABVSchedulerPolicy@2@@Z(ptr) Scheduler_Create
@ cdecl -arch=win64 ?Create@Scheduler@Concurrency@@SAPEAV12@AEBVSchedulerPolicy@2@@Z(ptr) Scheduler_Create
@ stub -arch=win32 ?CreateResourceManager@Concurrency@@YAPAUIResourceManager@1@XZ
@ stub -arch=win64 ?CreateResourceManager@Concurrency@@YAPEAUIResourceManager@1@XZ
@ cdecl -arch=win32 ?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPAVScheduleGroup@2@XZ() CurrentScheduler_CreateScheduleGroup
@ cdecl -arch=win64 ?CreateScheduleGroup@CurrentScheduler@Concurrency@@SAPEAVScheduleGroup@2@XZ() CurrentScheduler_CreateScheduleGroup
@ cdecl -arch=win32 ?CurrentContext@Context@Concurrency@@SAPAV12@XZ() Context_CurrentContext
@ cdecl -arch=win64 ?CurrentContext@Context@Concurrency@@SAPEAV12@XZ() Context_CurrentContext
@ cdecl ?Detach@CurrentScheduler@Concurrency@@SAXXZ() CurrentScheduler_Detach
@ stub ?DisableTracing@Concurrency@@YAJXZ
@ stub ?EnableTracing@Concurrency@@YAJXZ
@ cdecl -arch=win32 ?Free@Concurrency@@YAXPAX@Z(ptr) Concurrency_Free
@ cdecl -arch=win64 ?Free@Concurrency@@YAXPEAX@Z(ptr) Concurrency_Free
@ cdecl -arch=win32 ?Get@CurrentScheduler@Concurrency@@SAPAVScheduler@2@XZ() CurrentScheduler_Get
@ cdecl -arch=win64 ?Get@CurrentScheduler@Concurrency@@SAPEAVScheduler@2@XZ() CurrentScheduler_Get
@ stub ?GetExecutionContextId@Concurrency@@YAIXZ
@ cdecl ?GetNumberOfVirtualProcessors@CurrentScheduler@Concurrency@@SAIXZ() CurrentScheduler_GetNumberOfVirtualProcessors
@ stub ?GetOSVersion@Concurrency@@YA?AW4OSVersion@IResourceManager@1@XZ
@ cdecl ?GetPolicy@CurrentScheduler@Concurrency@@SA?AVSchedulerPolicy@2@XZ(ptr) CurrentScheduler_GetPolicy
@ thiscall -arch=i386 ?GetPolicyValue@SchedulerPolicy@Concurrency@@QBEIW4PolicyElementKey@2@@Z(ptr long) SchedulerPolicy_GetPolicyValue
@ cdecl -arch=win64 ?GetPolicyValue@SchedulerPolicy@Concurrency@@QEBAIW4PolicyElementKey@2@@Z(ptr long) SchedulerPolicy_GetPolicyValue
@ stub ?GetProcessorCount@Concurrency@@YAIXZ
@ stub ?GetProcessorNodeCount@Concurrency@@YAIXZ
@ stub ?GetSchedulerId@Concurrency@@YAIXZ
@ stub -arch=win32 ?GetSharedTimerQueue@details@Concurrency@@YAPAXXZ
@ stub -arch=win64 ?GetSharedTimerQueue@details@Concurrency@@YAPEAXXZ
@ cdecl ?Id@Context@Concurrency@@SAIXZ() Context_Id
@ cdecl ?Id@CurrentScheduler@Concurrency@@SAIXZ() CurrentScheduler_Id
@ cdecl ?IsCurrentTaskCollectionCanceling@Context@Concurrency@@SA_NXZ() Context_IsCurrentTaskCollectionCanceling
@ stub -arch=win32 ?Log2@details@Concurrency@@YAKI@Z
@ stub -arch=win64 ?Log2@details@Concurrency@@YAK_K@Z
@ cdecl ?Oversubscribe@Context@Concurrency@@SAX_N@Z(long) Context_Oversubscribe
@ cdecl -arch=win32 ?RegisterShutdownEvent@CurrentScheduler@Concurrency@@SAXPAX@Z(long) CurrentScheduler_RegisterShutdownEvent
@ cdecl -arch=win64 ?RegisterShutdownEvent@CurrentScheduler@Concurrency@@SAXPEAX@Z(long) CurrentScheduler_RegisterShutdownEvent
@ cdecl ?ResetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXXZ() Scheduler_ResetDefaultSchedulerPolicy
@ cdecl ?ScheduleGroupId@Context@Concurrency@@SAIXZ() Context_ScheduleGroupId
@ cdecl -arch=win32 ?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPAX@Z0@Z(ptr ptr) CurrentScheduler_ScheduleTask
@ cdecl -arch=win64 ?ScheduleTask@CurrentScheduler@Concurrency@@SAXP6AXPEAX@Z0@Z(ptr ptr) CurrentScheduler_ScheduleTask
@ thiscall -arch=i386 ?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QAEXII@Z(ptr long long) SchedulerPolicy_SetConcurrencyLimits
@ cdecl -arch=win64 ?SetConcurrencyLimits@SchedulerPolicy@Concurrency@@QEAAXII@Z(ptr long long) SchedulerPolicy_SetConcurrencyLimits
@ cdecl -arch=win32 ?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXABVSchedulerPolicy@2@@Z(ptr) Scheduler_SetDefaultSchedulerPolicy
@ cdecl -arch=win64 ?SetDefaultSchedulerPolicy@Scheduler@Concurrency@@SAXAEBVSchedulerPolicy@2@@Z(ptr) Scheduler_SetDefaultSchedulerPolicy
@ thiscall -arch=i386 ?SetPolicyValue@SchedulerPolicy@Concurrency@@QAEIW4PolicyElementKey@2@I@Z(ptr long long) SchedulerPolicy_SetPolicyValue
@ cdecl -arch=win64 ?SetPolicyValue@SchedulerPolicy@Concurrency@@QEAAIW4PolicyElementKey@2@I@Z(ptr long long) SchedulerPolicy_SetPolicyValue
@ cdecl ?VirtualProcessorId@Context@Concurrency@@SAIXZ() Context_VirtualProcessorId
@ cdecl ?Yield@Context@Concurrency@@SAXXZ() Context_Yield
@ stub -arch=win32 ?_Abort@_StructuredTaskCollection@details@Concurrency@@AAEXXZ
@ stub -arch=win64 ?_Abort@_StructuredTaskCollection@details@Concurrency@@AEAAXXZ
@ thiscall -arch=win32 ?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QAEXXZ(ptr) _ReentrantBlockingLock__Acquire
@ cdecl -arch=win64 ?_Acquire@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ(ptr) _ReentrantBlockingLock__Acquire
@ thiscall -arch=win32 ?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QAEXPAX@Z(ptr ptr) _NonReentrantPPLLock__Acquire
@ cdecl -arch=win64 ?_Acquire@_NonReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z(ptr ptr) _NonReentrantPPLLock__Acquire
@ thiscall -arch=win32 ?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QAEXXZ(ptr) _ReentrantBlockingLock__Acquire
@ cdecl -arch=win64 ?_Acquire@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ(ptr) _ReentrantBlockingLock__Acquire
@ stub -arch=win32 ?_Acquire@_ReentrantLock@details@Concurrency@@QAEXXZ
@ stub -arch=win64 ?_Acquire@_ReentrantLock@details@Concurrency@@QEAAXXZ
@ thiscall -arch=win32 ?_Acquire@_ReentrantPPLLock@details@Concurrency@@QAEXPAX@Z(ptr ptr) _ReentrantPPLLock__Acquire
@ cdecl -arch=win64 ?_Acquire@_ReentrantPPLLock@details@Concurrency@@QEAAXPEAX@Z(ptr ptr) _ReentrantPPLLock__Acquire
@ stub -arch=win32 ?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QAEXXZ
@ stub -arch=win64 ?_AcquireRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ
@ stub -arch=win32 ?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QAEXXZ
@ stub -arch=win64 ?_AcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ
@ stub -arch=win32 ?_Cancel@_StructuredTaskCollection@details@Concurrency@@QAEXXZ
@ stub -arch=win64 ?_Cancel@_StructuredTaskCollection@details@Concurrency@@QEAAXXZ
@ stub -arch=win32 ?_Cancel@_TaskCollection@details@Concurrency@@QAEXXZ
@ stub -arch=win64 ?_Cancel@_TaskCollection@details@Concurrency@@QEAAXXZ
@ stub -arch=win32 ?_CheckTaskCollection@_UnrealizedChore@details@Concurrency@@IAEXXZ
@ stub -arch=win64 ?_CheckTaskCollection@_UnrealizedChore@details@Concurrency@@IEAAXXZ
@ stub -arch=win32 ?_ConcRT_Assert@details@Concurrency@@YAXPBD0H@Z
@ stub -arch=win64 ?_ConcRT_Assert@details@Concurrency@@YAXPEBD0H@Z
@ stub -arch=win32 ?_ConcRT_CoreAssert@details@Concurrency@@YAXPBD0H@Z
@ stub -arch=win64 ?_ConcRT_CoreAssert@details@Concurrency@@YAXPEBD0H@Z
@ stub -arch=win32 ?_ConcRT_DumpMessage@details@Concurrency@@YAXPB_WZZ
@ stub -arch=win64 ?_ConcRT_DumpMessage@details@Concurrency@@YAXPEB_WZZ
@ stub -arch=win32 ?_ConcRT_Trace@details@Concurrency@@YAXHPB_WZZ
@ stub -arch=win64 ?_ConcRT_Trace@details@Concurrency@@YAXHPEB_WZZ
@ stub -arch=win32 ?_Copy_str@exception@std@@AAEXPBD@Z
@ stub -arch=win64 ?_Copy_str@exception@std@@AEAAXPEBD@Z
@ thiscall -arch=win32 ?_DoYield@?$_SpinWait@$00@details@Concurrency@@IAEXXZ(ptr) SpinWait__DoYield
@ cdecl -arch=win64 ?_DoYield@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ(ptr) SpinWait__DoYield
@ thiscall -arch=win32 ?_DoYield@?$_SpinWait@$0A@@details@Concurrency@@IAEXXZ(ptr) SpinWait__DoYield
@ cdecl -arch=win64 ?_DoYield@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ(ptr) SpinWait__DoYield
@ stub -arch=win32 ?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QAE_NXZ
@ stub -arch=win64 ?_IsCanceling@_StructuredTaskCollection@details@Concurrency@@QEAA_NXZ
@ stub -arch=win32 ?_IsCanceling@_TaskCollection@details@Concurrency@@QAE_NXZ
@ stub -arch=win64 ?_IsCanceling@_TaskCollection@details@Concurrency@@QEAA_NXZ
@ stub -arch=win32 ?_Name_base@type_info@@CAPBDPBV1@PAU__type_info_node@@@Z
@ stub -arch=win64 ?_Name_base@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z
@ stub -arch=win32 ?_Name_base_internal@type_info@@CAPBDPBV1@PAU__type_info_node@@@Z
@ stub -arch=win64 ?_Name_base_internal@type_info@@CAPEBDPEBV1@PEAU__type_info_node@@@Z
@ thiscall -arch=win32 ?_NumberOfSpins@?$_SpinWait@$00@details@Concurrency@@IAEKXZ(ptr) SpinWait__NumberOfSpins
@ cdecl -arch=win64 ?_NumberOfSpins@?$_SpinWait@$00@details@Concurrency@@IEAAKXZ(ptr) SpinWait__NumberOfSpins
@ thiscall -arch=win32 ?_NumberOfSpins@?$_SpinWait@$0A@@details@Concurrency@@IAEKXZ(ptr) SpinWait__NumberOfSpins
@ cdecl -arch=win64 ?_NumberOfSpins@?$_SpinWait@$0A@@details@Concurrency@@IEAAKXZ(ptr) SpinWait__NumberOfSpins
@ thiscall -arch=win32 ?_Release@_NonReentrantBlockingLock@details@Concurrency@@QAEXXZ(ptr) _ReentrantBlockingLock__Release
@ cdecl -arch=win64 ?_Release@_NonReentrantBlockingLock@details@Concurrency@@QEAAXXZ(ptr) _ReentrantBlockingLock__Release
@ thiscall -arch=win32 ?_Release@_NonReentrantPPLLock@details@Concurrency@@QAEXXZ(ptr) _NonReentrantPPLLock__Release
@ cdecl -arch=win64 ?_Release@_NonReentrantPPLLock@details@Concurrency@@QEAAXXZ(ptr) _NonReentrantPPLLock__Release
@ thiscall -arch=win32 ?_Release@_ReentrantBlockingLock@details@Concurrency@@QAEXXZ(ptr) _ReentrantBlockingLock__Release
@ cdecl -arch=win64 ?_Release@_ReentrantBlockingLock@details@Concurrency@@QEAAXXZ(ptr) _ReentrantBlockingLock__Release
@ stub -arch=win32 ?_Release@_ReentrantLock@details@Concurrency@@QAEXXZ
@ stub -arch=win64 ?_Release@_ReentrantLock@details@Concurrency@@QEAAXXZ
@ thiscall -arch=win32 ?_Release@_ReentrantPPLLock@details@Concurrency@@QAEXXZ(ptr) _ReentrantPPLLock__Release
@ cdecl -arch=win64 ?_Release@_ReentrantPPLLock@details@Concurrency@@QEAAXXZ(ptr) _ReentrantPPLLock__Release
@ stub -arch=win32 ?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QAEXXZ
@ stub -arch=win64 ?_ReleaseRead@_ReaderWriterLock@details@Concurrency@@QEAAXXZ
@ stub -arch=win32 ?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QAEXXZ
@ stub -arch=win64 ?_ReleaseWrite@_ReaderWriterLock@details@Concurrency@@QEAAXXZ
@ thiscall -arch=win32 ?_Reset@?$_SpinWait@$00@details@Concurrency@@IAEXXZ(ptr) SpinWait__Reset
@ cdecl -arch=win64 ?_Reset@?$_SpinWait@$00@details@Concurrency@@IEAAXXZ(ptr) SpinWait__Reset
@ thiscall -arch=win32 ?_Reset@?$_SpinWait@$0A@@details@Concurrency@@IAEXXZ(ptr) SpinWait__Reset
@ cdecl -arch=win64 ?_Reset@?$_SpinWait@$0A@@details@Concurrency@@IEAAXXZ(ptr) SpinWait__Reset
@ stub -arch=win32 ?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QAG?AW4_TaskCollectionStatus@23@PAV_UnrealizedChore@23@@Z
@ stub -arch=win64 ?_RunAndWait@_StructuredTaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z
@ stub -arch=win32 ?_RunAndWait@_TaskCollection@details@Concurrency@@QAG?AW4_TaskCollectionStatus@23@PAV_UnrealizedChore@23@@Z
@ stub -arch=win64 ?_RunAndWait@_TaskCollection@details@Concurrency@@QEAA?AW4_TaskCollectionStatus@23@PEAV_UnrealizedChore@23@@Z
@ stub -arch=win32 ?_Schedule@_StructuredTaskCollection@details@Concurrency@@QAEXPAV_UnrealizedChore@23@@Z
@ stub -arch=win64 ?_Schedule@_StructuredTaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z
@ stub -arch=win32 ?_Schedule@_TaskCollection@details@Concurrency@@QAEXPAV_UnrealizedChore@23@@Z
@ stub -arch=win64 ?_Schedule@_TaskCollection@details@Concurrency@@QEAAXPEAV_UnrealizedChore@23@@Z
@ thiscall -arch=win32 ?_SetSpinCount@?$_SpinWait@$00@details@Concurrency@@QAEXI@Z(ptr long) SpinWait__SetSpinCount
@ cdecl -arch=win64 ?_SetSpinCount@?$_SpinWait@$00@details@Concurrency@@QEAAXI@Z(ptr long) SpinWait__SetSpinCount
@ thiscall -arch=win32 ?_SetSpinCount@?$_SpinWait@$0A@@details@Concurrency@@QAEXI@Z(ptr long) SpinWait__SetSpinCount
@ cdecl -arch=win64 ?_SetSpinCount@?$_SpinWait@$0A@@details@Concurrency@@QEAAXI@Z(ptr long) SpinWait__SetSpinCount
@ thiscall -arch=win32 ?_ShouldSpinAgain@?$_SpinWait@$00@details@Concurrency@@IAE_NXZ(ptr) SpinWait__ShouldSpinAgain
@ cdecl -arch=win64 ?_ShouldSpinAgain@?$_SpinWait@$00@details@Concurrency@@IEAA_NXZ(ptr) SpinWait__ShouldSpinAgain
@ thiscall -arch=win32 ?_ShouldSpinAgain@?$_SpinWait@$0A@@details@Concurrency@@IAE_NXZ(ptr) SpinWait__ShouldSpinAgain
@ cdecl -arch=win64 ?_ShouldSpinAgain@?$_SpinWait@$0A@@details@Concurrency@@IEAA_NXZ(ptr) SpinWait__ShouldSpinAgain
@ thiscall -arch=win32 ?_SpinOnce@?$_SpinWait@$00@details@Concurrency@@QAE_NXZ(ptr) SpinWait__SpinOnce
@ cdecl -arch=win64 ?_SpinOnce@?$_SpinWait@$00@details@Concurrency@@QEAA_NXZ(ptr) SpinWait__SpinOnce
@ thiscall -arch=win32 ?_SpinOnce@?$_SpinWait@$0A@@details@Concurrency@@QAE_NXZ(ptr) SpinWait__SpinOnce
@ cdecl -arch=win64 ?_SpinOnce@?$_SpinWait@$0A@@details@Concurrency@@QEAA_NXZ(ptr) SpinWait__SpinOnce
@ cdecl ?_SpinYield@Context@Concurrency@@SAXXZ() Context__SpinYield
@ thiscall -arch=win32 ?_Start@_Timer@details@Concurrency@@IAEXXZ(ptr) _Timer__Start
@ cdecl -arch=win64 ?_Start@_Timer@details@Concurrency@@IEAAXXZ(ptr) _Timer__Start
@ thiscall -arch=win32 ?_Stop@_Timer@details@Concurrency@@IAEXXZ(ptr) _Timer__Stop
@ cdecl -arch=win64 ?_Stop@_Timer@details@Concurrency@@IEAAXXZ(ptr) _Timer__Stop
@ stub -arch=win32 ?_Tidy@exception@std@@AAEXXZ
@ stub -arch=win64 ?_Tidy@exception@std@@AEAAXXZ
@ cdecl -arch=win32 ?_Trace_ppl_function@Concurrency@@YAXABU_GUID@@EW4ConcRT_EventType@1@@Z(ptr long long) _Trace_ppl_function
@ cdecl -arch=win64 ?_Trace_ppl_function@Concurrency@@YAXAEBU_GUID@@EW4ConcRT_EventType@1@@Z(ptr long long) _Trace_ppl_function
@ thiscall -arch=win32 ?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QAE_NXZ(ptr) _ReentrantBlockingLock__TryAcquire
@ cdecl -arch=win64 ?_TryAcquire@_NonReentrantBlockingLock@details@Concurrency@@QEAA_NXZ(ptr) _ReentrantBlockingLock__TryAcquire
@ thiscall -arch=win32 ?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QAE_NXZ(ptr) _ReentrantBlockingLock__TryAcquire
@ cdecl -arch=win64 ?_TryAcquire@_ReentrantBlockingLock@details@Concurrency@@QEAA_NXZ(ptr) _ReentrantBlockingLock__TryAcquire
@ stub -arch=win32 ?_TryAcquire@_ReentrantLock@details@Concurrency@@QAE_NXZ
@ stub -arch=win64 ?_TryAcquire@_ReentrantLock@details@Concurrency@@QEAA_NXZ
@ stub -arch=win32 ?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QAE_NXZ
@ stub -arch=win64 ?_TryAcquireWrite@_ReaderWriterLock@details@Concurrency@@QEAA_NXZ
@ stub -arch=win32 ?_Type_info_dtor@type_info@@CAXPAV1@@Z
@ stub -arch=win64 ?_Type_info_dtor@type_info@@CAXPEAV1@@Z
@ stub -arch=win32 ?_Type_info_dtor_internal@type_info@@CAXPAV1@@Z
@ stub -arch=win64 ?_Type_info_dtor_internal@type_info@@CAXPEAV1@@Z
@ stub -arch=win32 ?_UnderlyingYield@details@Concurrency@@YAXXZ
@ stub -arch=win64 ?_ValidateExecute@@YAHP6A_JXZ@Z
@ stub ?_ValidateExecute@@YAHP6GHXZ@Z
@ stub -arch=win32 ?_ValidateRead@@YAHPBXI@Z
@ stub -arch=win64 ?_ValidateRead@@YAHPEBXI@Z
@ stub -arch=win32 ?_ValidateWrite@@YAHPAXI@Z
@ stub -arch=win64 ?_ValidateWrite@@YAHPEAXI@Z
@ cdecl ?_Value@_SpinCount@details@Concurrency@@SAIXZ() SpinCount__Value
@ cdecl -arch=win32 ?__ExceptionPtrAssign@@YAXPAXPBX@Z(ptr ptr) __ExceptionPtrAssign
@ cdecl -arch=win64 ?__ExceptionPtrAssign@@YAXPEAXPEBX@Z(ptr ptr) __ExceptionPtrAssign
@ cdecl -arch=win32 ?__ExceptionPtrCompare@@YA_NPBX0@Z(ptr ptr) __ExceptionPtrCompare
@ cdecl -arch=win64 ?__ExceptionPtrCompare@@YA_NPEBX0@Z(ptr ptr) __ExceptionPtrCompare
@ cdecl -arch=win32 ?__ExceptionPtrCopy@@YAXPAXPBX@Z(ptr ptr) __ExceptionPtrCopy
@ cdecl -arch=win64 ?__ExceptionPtrCopy@@YAXPEAXPEBX@Z(ptr ptr) __ExceptionPtrCopy
@ cdecl -arch=win32 ?__ExceptionPtrCopyException@@YAXPAXPBX1@Z(ptr ptr ptr) __ExceptionPtrCopyException
@ cdecl -arch=win64 ?__ExceptionPtrCopyException@@YAXPEAXPEBX1@Z(ptr ptr ptr) __ExceptionPtrCopyException
@ cdecl -arch=win32 ?__ExceptionPtrCreate@@YAXPAX@Z(ptr) __ExceptionPtrCreate
@ cdecl -arch=win64 ?__ExceptionPtrCreate@@YAXPEAX@Z(ptr) __ExceptionPtrCreate
@ cdecl -arch=win32 ?__ExceptionPtrCurrentException@@YAXPAX@Z(ptr) __ExceptionPtrCurrentException
@ cdecl -arch=win64 ?__ExceptionPtrCurrentException@@YAXPEAX@Z(ptr) __ExceptionPtrCurrentException
@ cdecl -arch=win32 ?__ExceptionPtrDestroy@@YAXPAX@Z(ptr) __ExceptionPtrDestroy
@ cdecl -arch=win64 ?__ExceptionPtrDestroy@@YAXPEAX@Z(ptr) __ExceptionPtrDestroy
@ cdecl -arch=win32 ?__ExceptionPtrRethrow@@YAXPBX@Z(ptr) __ExceptionPtrRethrow
@ cdecl -arch=win64 ?__ExceptionPtrRethrow@@YAXPEBX@Z(ptr) __ExceptionPtrRethrow
@ cdecl __uncaught_exception()
@ stub ?_inconsistency@@YAXXZ
@ cdecl -arch=win32 ?_invalid_parameter@@YAXPBG00II@Z(wstr wstr wstr long long) _invalid_parameter
@ cdecl -arch=win64 ?_invalid_parameter@@YAXPEBG00I_K@Z(wstr wstr wstr long long) _invalid_parameter
@ cdecl -arch=win32 ?_is_exception_typeof@@YAHABVtype_info@@PAU_EXCEPTION_POINTERS@@@Z(ptr ptr) _is_exception_typeof
@ cdecl -arch=win64 ?_is_exception_typeof@@YAHAEBVtype_info@@PEAU_EXCEPTION_POINTERS@@@Z(ptr ptr) _is_exception_typeof
@ cdecl -arch=arm ?_name_internal_method@type_info@@QBAPBDPAU__type_info_node@@@Z(ptr ptr) type_info_name_internal_method
@ thiscall -arch=i386 ?_name_internal_method@type_info@@QBEPBDPAU__type_info_node@@@Z(ptr ptr) type_info_name_internal_method
@ cdecl -arch=win64 ?_name_internal_method@type_info@@QEBAPEBDPEAU__type_info_node@@@Z(ptr ptr) type_info_name_internal_method
@ varargs -arch=win32 ?_open@@YAHPBDHH@Z(str long) _open
@ varargs -arch=win64 ?_open@@YAHPEBDHH@Z(str long) _open
@ cdecl -arch=win32 ?_query_new_handler@@YAP6AHI@ZXZ() _query_new_handler
@ cdecl -arch=win64 ?_query_new_handler@@YAP6AH_K@ZXZ() _query_new_handler
@ cdecl ?_query_new_mode@@YAHXZ() _query_new_mode
@ stub -arch=win32 ?_set_new_handler@@YAP6AHI@ZH@Z  # int (__cdecl*__cdecl _set_new_handler(int))(unsigned int)
@ stub -arch=win64 ?_set_new_handler@@YAP6AH_K@ZH@Z  # int (__cdecl*__cdecl _set_new_handler(int))(unsigned __int64)
@ cdecl -arch=win32 ?_set_new_handler@@YAP6AHI@ZP6AHI@Z@Z(ptr) _set_new_handler
@ cdecl -arch=win64 ?_set_new_handler@@YAP6AH_K@ZP6AH0@Z@Z(ptr) _set_new_handler
@ cdecl ?_set_new_mode@@YAHH@Z(long) _set_new_mode
@ stub -arch=win32 ?_set_se_translator@@YAP6AXIPAU_EXCEPTION_POINTERS@@@ZH@Z  # void (__cdecl*__cdecl _set_se_translator(int))(unsigned int,struct _EXCEPTION_POINTERS *)
@ stub -arch=win64 ?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZH@Z  # void (__cdecl*__cdecl _set_se_translator(int))(unsigned int,struct _EXCEPTION_POINTERS * __ptr64)
@ cdecl -arch=win32 ?_set_se_translator@@YAP6AXIPAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z(ptr) _set_se_translator
@ cdecl -arch=win64 ?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z(ptr) _set_se_translator
@ cdecl -arch=win32 ?_sopen@@YAHPBDHHH@Z(str long long long) _sopen
@ cdecl -arch=win64 ?_sopen@@YAHPEBDHHH@Z(str long long long) _sopen
@ stub -arch=win32 ?_type_info_dtor_internal_method@type_info@@QAEXXZ  # public: void __thiscall type_info::_type_info_dtor_internal_method(void)
@ stub -arch=win64 ?_type_info_dtor_internal_method@type_info@@QEAAXXZ  # public: void __cdecl type_info::_type_info_dtor_internal_method(void) __ptr64
@ cdecl -arch=win32 ?_wopen@@YAHPB_WHH@Z(wstr long long) _wopen
@ cdecl -arch=win64 ?_wopen@@YAHPEB_WHH@Z(wstr long long) _wopen
@ cdecl -arch=win32 ?_wsopen@@YAHPB_WHHH@Z(wstr long long long) _wsopen
@ cdecl -arch=win64 ?_wsopen@@YAHPEB_WHHH@Z(wstr long long long) _wsopen
@ thiscall -arch=i386 ?before@type_info@@QBEHABV1@@Z(ptr ptr) type_info_before
@ cdecl -arch=win64 ?before@type_info@@QEBAHAEBV1@@Z(ptr ptr) type_info_before
@ thiscall -arch=i386 ?get_error_code@scheduler_resource_allocation_error@Concurrency@@QBEJXZ(ptr) scheduler_resource_allocation_error_get_error_code
@ cdecl -arch=win64 ?get_error_code@scheduler_resource_allocation_error@Concurrency@@QEBAJXZ(ptr) scheduler_resource_allocation_error_get_error_code
@ thiscall -arch=win32 ?lock@critical_section@Concurrency@@QAEXXZ(ptr) critical_section_lock
@ cdecl -arch=win64 ?lock@critical_section@Concurrency@@QEAAXXZ(ptr) critical_section_lock
@ thiscall -arch=win32 ?lock@reader_writer_lock@Concurrency@@QAEXXZ(ptr) reader_writer_lock_lock
@ cdecl -arch=win64 ?lock@reader_writer_lock@Concurrency@@QEAAXXZ(ptr) reader_writer_lock_lock
@ thiscall -arch=win32 ?lock_read@reader_writer_lock@Concurrency@@QAEXXZ(ptr) reader_writer_lock_lock_read
@ cdecl -arch=win64 ?lock_read@reader_writer_lock@Concurrency@@QEAAXXZ(ptr) reader_writer_lock_lock_read
@ thiscall -arch=win32 ?name@type_info@@QBEPBDPAU__type_info_node@@@Z(ptr ptr) type_info_name_internal_method
@ cdecl -arch=win64 ?name@type_info@@QEBAPEBDPEAU__type_info_node@@@Z(ptr ptr) type_info_name_internal_method
@ thiscall -arch=win32 ?native_handle@critical_section@Concurrency@@QAEAAV12@XZ(ptr) critical_section_native_handle
@ cdecl -arch=win64 ?native_handle@critical_section@Concurrency@@QEAAAEAV12@XZ(ptr) critical_section_native_handle
@ cdecl -arch=arm ?raw_name@type_info@@QBAPBDXZ(ptr) type_info_raw_name
@ thiscall -arch=i386 ?raw_name@type_info@@QBEPBDXZ(ptr) type_info_raw_name
@ cdecl -arch=win64 ?raw_name@type_info@@QEBAPEBDXZ(ptr) type_info_raw_name
@ thiscall -arch=win32 ?reset@event@Concurrency@@QAEXXZ(ptr) event_reset
@ cdecl -arch=win64 ?reset@event@Concurrency@@QEAAXXZ(ptr) event_reset
@ thiscall -arch=win32 ?set@event@Concurrency@@QAEXXZ(ptr) event_set
@ cdecl -arch=win64 ?set@event@Concurrency@@QEAAXXZ(ptr) event_set
@ cdecl ?set_new_handler@@YAP6AXXZP6AXXZ@Z(ptr) set_new_handler
@ stub ?set_terminate@@YAP6AXXZH@Z
@ cdecl ?set_terminate@@YAP6AXXZP6AXXZ@Z(ptr) set_terminate
@ stub ?set_unexpected@@YAP6AXXZH@Z
@ cdecl ?set_unexpected@@YAP6AXXZP6AXXZ@Z(ptr) set_unexpected
@ varargs ?swprintf@@YAHPAGIPBGZZ(ptr long wstr) _snwprintf
@ varargs ?swprintf@@YAHPA_WIPB_WZZ(ptr long wstr) _snwprintf
@ cdecl ?terminate@@YAXXZ() terminate
@ thiscall -arch=win32 ?try_lock@critical_section@Concurrency@@QAE_NXZ(ptr) critical_section_try_lock
@ cdecl -arch=win64 ?try_lock@critical_section@Concurrency@@QEAA_NXZ(ptr) critical_section_try_lock
@ thiscall -arch=win32 ?try_lock@reader_writer_lock@Concurrency@@QAE_NXZ(ptr) reader_writer_lock_try_lock
@ cdecl -arch=win64 ?try_lock@reader_writer_lock@Concurrency@@QEAA_NXZ(ptr) reader_writer_lock_try_lock
@ thiscall -arch=win32 ?try_lock_read@reader_writer_lock@Concurrency@@QAE_NXZ(ptr) reader_writer_lock_try_lock_read
@ cdecl -arch=win64 ?try_lock_read@reader_writer_lock@Concurrency@@QEAA_NXZ(ptr) reader_writer_lock_try_lock_read
@ cdecl ?unexpected@@YAXXZ() unexpected
@ thiscall -arch=win32 ?unlock@critical_section@Concurrency@@QAEXXZ(ptr) critical_section_unlock
@ cdecl -arch=win64 ?unlock@critical_section@Concurrency@@QEAAXXZ(ptr) critical_section_unlock
@ thiscall -arch=win32 ?unlock@reader_writer_lock@Concurrency@@QAEXXZ(ptr) reader_writer_lock_unlock
@ cdecl -arch=win64 ?unlock@reader_writer_lock@Concurrency@@QEAAXXZ(ptr) reader_writer_lock_unlock
@ cdecl ?vswprintf@@YAHPA_WIPB_WPAD@Z(ptr long wstr ptr) _vsnwprintf
@ cdecl ?wait@Concurrency@@YAXI@Z(long) Concurrency_wait
@ thiscall -arch=win32 ?wait@event@Concurrency@@QAEII@Z(ptr long) event_wait
@ cdecl -arch=win64 ?wait@event@Concurrency@@QEAA_KI@Z(ptr long) event_wait
@ cdecl -arch=win32 ?wait_for_multiple@event@Concurrency@@SAIPAPAV12@I_NI@Z(ptr long long long) event_wait_for_multiple
@ cdecl -arch=win64 ?wait_for_multiple@event@Concurrency@@SA_KPEAPEAV12@_K_NI@Z(ptr long long long) event_wait_for_multiple
@ thiscall -arch=i386 ?what@exception@std@@UBEPBDXZ(ptr) exception_what
@ cdecl -arch=win64 ?what@exception@std@@UEBAPEBDXZ(ptr) exception_what
@ cdecl -norelay $I10_OUTPUT(double long long long ptr) I10_OUTPUT
@ cdecl -arch=i386 _CIacos()
@ cdecl -arch=i386 _CIasin()
@ cdecl -arch=i386 _CIatan()
@ cdecl -arch=i386 _CIatan2()
@ cdecl -arch=i386 _CIcos()
@ cdecl -arch=i386 _CIcosh()
@ cdecl -arch=i386 _CIexp()
@ cdecl -arch=i386 _CIfmod()
@ cdecl -arch=i386 _CIlog()
@ cdecl -arch=i386 _CIlog10()
@ cdecl -arch=i386 _CIpow()
@ cdecl -arch=i386 _CIsin()
@ cdecl -arch=i386 _CIsinh()
@ cdecl -arch=i386 _CIsqrt()
@ cdecl -arch=i386 _CItan()
@ cdecl -arch=i386 _CItanh()
@ cdecl _CRT_RTC_INIT(ptr ptr long long long)
@ cdecl _CRT_RTC_INITW(ptr ptr long long long)
@ cdecl _CreateFrameInfo(ptr ptr)
@ stdcall _CxxThrowException(ptr ptr)
@ cdecl -arch=i386 -norelay _EH_prolog()
@ cdecl _FindAndUnlinkFrame(ptr)
@ cdecl _Getdays()
@ cdecl _Getmonths()
@ cdecl _Gettnames()
@ extern _HUGE MSVCRT__HUGE
@ cdecl _IsExceptionObjectToBeDestroyed(ptr)
@ stub _NLG_Dispatch2
@ stub _NLG_Return
@ stub _NLG_Return2
@ stub -arch=win64 _SetImageBase
@ stub -arch=win64 _SetThrowImageBase
@ cdecl _Strftime(ptr long str ptr ptr)
@ cdecl _XcptFilter(long ptr)
@ cdecl __AdjustPointer(ptr ptr)
@ stub __BuildCatchObject
@ stub __BuildCatchObjectHelper
@ stdcall -arch=x86_64 __C_specific_handler(ptr long ptr ptr) ntdll.__C_specific_handler
@ cdecl -arch=i386,x86_64,arm,arm64 __CppXcptFilter(long ptr)
@ stub __CxxCallUnwindDelDtor
@ stub __CxxCallUnwindDtor
@ stub __CxxCallUnwindStdDelDtor
@ stub __CxxCallUnwindVecDtor
@ cdecl -arch=i386,x86_64,arm,arm64 __CxxDetectRethrow(ptr)
@ cdecl -arch=i386,x86_64,arm,arm64 __CxxExceptionFilter(ptr ptr long ptr)
@ cdecl -arch=i386,x86_64,arm,arm64 -norelay __CxxFrameHandler(ptr ptr ptr ptr)
@ cdecl -arch=i386,x86_64,arm,arm64 -norelay __CxxFrameHandler2(ptr ptr ptr ptr) __CxxFrameHandler
@ cdecl -arch=i386,x86_64,arm,arm64 -norelay __CxxFrameHandler3(ptr ptr ptr ptr) __CxxFrameHandler
@ stdcall -arch=i386 __CxxLongjmpUnwind(ptr)
@ cdecl -arch=i386,x86_64,arm,arm64 __CxxQueryExceptionSize()
@ cdecl __CxxRegisterExceptionObject(ptr ptr)
@ cdecl __CxxUnregisterExceptionObject(ptr long)
@ cdecl __DestructExceptionObject(ptr)
@ stub __FrameUnwindFilter
@ cdecl __RTCastToVoid(ptr)
@ cdecl __RTDynamicCast(ptr long ptr ptr long)
@ cdecl __RTtypeid(ptr)
@ cdecl __STRINGTOLD(ptr ptr str long)
@ cdecl __STRINGTOLD_L(ptr ptr str long ptr)
@ stub __TypeMatch
@ cdecl ___lc_codepage_func()
@ cdecl ___lc_collate_cp_func()
@ cdecl ___lc_handle_func()
@ cdecl ___mb_cur_max_func()
@ cdecl ___mb_cur_max_l_func(ptr)
@ cdecl ___setlc_active_func()
@ cdecl ___unguarded_readlc_active_add_func()
@ extern __argc MSVCRT___argc
@ extern __argv MSVCRT___argv
@ extern __badioinfo MSVCRT___badioinfo
@ cdecl __clean_type_info_names_internal(ptr)
@ cdecl -arch=i386 __control87_2(long long ptr ptr)
@ cdecl __create_locale(long str) _create_locale
@ cdecl __crtCompareStringA(long long str long str long)
@ cdecl __crtCompareStringW(long long wstr long wstr long)
@ cdecl __crtLCMapStringA(long long str long ptr long long long)
@ cdecl __crtLCMapStringW(long long wstr long ptr long long long)
@ cdecl __daylight() __p__daylight
@ cdecl __dllonexit(ptr ptr ptr)
@ cdecl __doserrno()
@ cdecl __dstbias() __p__dstbias
@ stub ___fls_getvalue@4
@ stub ___fls_setvalue@8
@ cdecl __fpecode()
@ cdecl __free_locale(ptr) _free_locale
@ cdecl __get_current_locale() _get_current_locale
@ stub __get_flsindex
@ stub __get_tlsindex
@ cdecl __getmainargs(ptr ptr ptr long ptr)
@ extern __initenv MSVCRT___initenv
@ cdecl __iob_func()
@ cdecl __isascii(long)
@ cdecl __iscsym(long)
@ cdecl __iscsymf(long)
@ stub __iswcsym
@ stub __iswcsymf
# extern __lconv
@ cdecl __lconv_init()
@ cdecl -arch=i386 -norelay __libm_sse2_acos()
@ cdecl -arch=i386 -norelay __libm_sse2_acosf()
@ cdecl -arch=i386 -norelay __libm_sse2_asin()
@ cdecl -arch=i386 -norelay __libm_sse2_asinf()
@ cdecl -arch=i386 -norelay __libm_sse2_atan()
@ cdecl -arch=i386 -norelay __libm_sse2_atan2()
@ cdecl -arch=i386 -norelay __libm_sse2_atanf()
@ cdecl -arch=i386 -norelay __libm_sse2_cos()
@ cdecl -arch=i386 -norelay __libm_sse2_cosf()
@ cdecl -arch=i386 -norelay __libm_sse2_exp()
@ cdecl -arch=i386 -norelay __libm_sse2_expf()
@ cdecl -arch=i386 -norelay __libm_sse2_log()
@ cdecl -arch=i386 -norelay __libm_sse2_log10()
@ cdecl -arch=i386 -norelay __libm_sse2_log10f()
@ cdecl -arch=i386 -norelay __libm_sse2_logf()
@ cdecl -arch=i386 -norelay __libm_sse2_pow()
@ cdecl -arch=i386 -norelay __libm_sse2_powf()
@ cdecl -arch=i386 -norelay __libm_sse2_sin()
@ cdecl -arch=i386 -norelay __libm_sse2_sinf()
@ cdecl -arch=i386 -norelay __libm_sse2_tan()
@ cdecl -arch=i386 -norelay __libm_sse2_tanf()
@ extern __mb_cur_max MSVCRT___mb_cur_max
@ cdecl __p___argc()
@ cdecl __p___argv()
@ cdecl __p___initenv()
@ cdecl __p___mb_cur_max()
@ cdecl __p___wargv()
@ cdecl __p___winitenv()
@ cdecl __p__acmdln()
@ cdecl __p__commode()
@ cdecl __p__daylight()
@ cdecl __p__dstbias()
@ cdecl __p__environ()
@ cdecl __p__fmode()
@ cdecl __p__iob() __iob_func
@ stub __p__mbcasemap()
@ cdecl __p__mbctype()
@ cdecl __p__pctype()
@ cdecl __p__pgmptr()
@ cdecl __p__pwctype()
@ cdecl __p__timezone()
@ cdecl __p__tzname()
@ cdecl __p__wcmdln()
@ cdecl __p__wenviron()
@ cdecl __p__wpgmptr()
@ cdecl __pctype_func()
@ extern __pioinfo MSVCRT___pioinfo
@ cdecl __pwctype_func()
@ cdecl __pxcptinfoptrs()
@ stub __report_gsfailure
@ cdecl __set_app_type(long)
@ stub __set_flsgetvalue
@ extern __setlc_active MSVCRT___setlc_active
@ cdecl __setusermatherr(ptr)
@ cdecl __strncnt(str long)
@ varargs __swprintf_l(ptr wstr ptr)
@ cdecl __sys_errlist()
@ cdecl __sys_nerr()
@ cdecl __threadhandle() kernel32.GetCurrentThread
@ cdecl __threadid() kernel32.GetCurrentThreadId
@ cdecl __timezone() __p__timezone
@ cdecl __toascii(long)
@ cdecl __tzname() __p__tzname
@ cdecl __unDName(ptr str long ptr ptr long)
@ cdecl __unDNameEx(ptr str long ptr ptr ptr long)
@ stub __unDNameHelper
@ extern __unguarded_readlc_active MSVCRT___unguarded_readlc_active
@ cdecl __vswprintf_l(ptr wstr ptr ptr) _vswprintf_l
@ extern __wargv MSVCRT___wargv
@ cdecl __wcserror(wstr)
@ cdecl __wcserror_s(ptr long wstr)
@ stub __wcsncnt
@ cdecl __wgetmainargs(ptr ptr ptr long ptr)
@ extern __winitenv MSVCRT___winitenv
@ cdecl _abnormal_termination() __intrinsic_abnormal_termination
@ cdecl -ret64 _abs64(int64)
@ cdecl _access(str long)
@ cdecl _access_s(str long)
@ extern _acmdln MSVCRT__acmdln
@ cdecl _aligned_free(ptr)
@ cdecl _aligned_malloc(long long)
@ cdecl _aligned_msize(ptr long long)
@ cdecl _aligned_offset_malloc(long long long)
@ cdecl _aligned_offset_realloc(ptr long long long)
@ stub _aligned_offset_recalloc
@ cdecl _aligned_realloc(ptr long long)
@ stub _aligned_recalloc
@ cdecl _amsg_exit(long)
@ cdecl _assert(str str long)
@ cdecl _atodbl(ptr str)
@ cdecl _atodbl_l(ptr str ptr)
@ cdecl _atof_l(str ptr)
@ cdecl _atoflt(ptr str)
@ cdecl _atoflt_l(ptr str ptr)
@ cdecl -ret64 _atoi64(str)
@ cdecl -ret64 _atoi64_l(str ptr)
@ cdecl _atoi_l(str ptr)
@ cdecl _atol_l(str ptr)
@ cdecl _atoldbl(ptr str)
@ cdecl _atoldbl_l(ptr str ptr)
@ cdecl _beep(long long)
@ cdecl _beginthread(ptr long ptr)
@ cdecl _beginthreadex(ptr long ptr ptr long ptr)
@ cdecl _byteswap_uint64(int64)
@ cdecl _byteswap_ulong(long)
@ cdecl _byteswap_ushort(long)
@ cdecl _c_exit()
@ cdecl _cabs(long)
@ cdecl _callnewh(long)
@ cdecl _calloc_crt(long long) calloc
@ cdecl _cexit()
@ cdecl _cgets(ptr)
@ stub _cgets_s
@ stub _cgetws
@ stub _cgetws_s
@ cdecl _chdir(str)
@ cdecl _chdrive(long)
@ cdecl _chgsign(double)
@ cdecl -arch=!i386 _chgsignf(float)
@ cdecl -arch=i386 -norelay _chkesp()
@ cdecl _chmod(str long)
@ cdecl _chsize(long long)
@ cdecl _chsize_s(long int64)
@ cdecl _clearfp()
@ cdecl _close(long)
@ cdecl _commit(long)
@ extern _commode MSVCRT__commode
@ cdecl _configthreadlocale(long)
@ cdecl _control87(long long)
@ cdecl _controlfp(long long)
@ cdecl _controlfp_s(ptr long long)
@ cdecl _copysign(double double)
@ cdecl -arch=!i386 _copysignf(float float)
@ varargs _cprintf(str)
@ stub _cprintf_l
@ stub _cprintf_p
@ stub _cprintf_p_l
@ stub _cprintf_s
@ stub _cprintf_s_l
@ cdecl _cputs(str)
@ cdecl _cputws(wstr)
@ cdecl _creat(str long)
@ cdecl _create_locale(long str)
@ cdecl -arch=i386 _crt_debugger_hook(long)
@ cdecl -arch=arm,win64 __crt_debugger_hook(long) _crt_debugger_hook
@ varargs _cscanf(str)
@ varargs _cscanf_l(str ptr)
@ varargs _cscanf_s(str)
@ varargs _cscanf_s_l(str ptr)
@ cdecl _ctime32(ptr)
@ cdecl _ctime32_s(str long ptr)
@ cdecl _ctime64(ptr)
@ cdecl _ctime64_s(str long ptr)
@ cdecl _cwait(ptr long long)
@ varargs _cwprintf(wstr)
@ stub _cwprintf_l
@ stub _cwprintf_p
@ stub _cwprintf_p_l
@ stub _cwprintf_s
@ stub _cwprintf_s_l
@ varargs _cwscanf(wstr)
@ varargs _cwscanf_l(wstr ptr)
@ varargs _cwscanf_s(wstr)
@ varargs _cwscanf_s_l(wstr ptr)
@ extern _daylight MSVCRT___daylight
@ cdecl _difftime32(long long)
@ cdecl _difftime64(int64 int64)
@ stub _dosmaperr
@ extern _dstbias MSVCRT__dstbias
@ cdecl _dup(long)
@ cdecl _dup2(long long)
@ cdecl _dupenv_s(ptr ptr str)
@ cdecl _ecvt(double long ptr ptr)
@ cdecl _ecvt_s(str long double long ptr ptr)
@ cdecl _encoded_null()
@ cdecl _endthread()
@ cdecl _endthreadex(long)
@ extern _environ MSVCRT__environ
@ cdecl _eof(long)
@ cdecl _errno()
@ cdecl -arch=i386 _except_handler2(ptr ptr ptr ptr)
@ cdecl -arch=i386 _except_handler3(ptr ptr ptr ptr)
@ cdecl -arch=i386 _except_handler4_common(ptr ptr ptr ptr ptr ptr)
@ varargs _execl(str str)
@ varargs _execle(str str)
@ varargs _execlp(str str)
@ varargs _execlpe(str str)
@ cdecl _execv(str ptr)
@ cdecl _execve(str ptr ptr)
@ cdecl _execvp(str ptr)
@ cdecl _execvpe(str ptr ptr)
@ cdecl _exit(long)
@ cdecl _expand(ptr long)
@ cdecl _fclose_nolock(ptr)
@ cdecl _fcloseall()
@ cdecl _fcvt(double long ptr ptr)
@ cdecl _fcvt_s(ptr long double long ptr ptr)
@ cdecl _fdopen(long str)
@ cdecl _fflush_nolock(ptr)
@ cdecl _fgetc_nolock(ptr)
@ cdecl _fgetchar()
@ cdecl _fgetwc_nolock(ptr)
@ cdecl _fgetwchar()
@ cdecl _filbuf(ptr)
@ cdecl _filelength(long)
@ cdecl -ret64 _filelengthi64(long)
@ cdecl _fileno(ptr)
@ cdecl _findclose(long)
@ cdecl _findfirst32(str ptr)
@ stub _findfirst32i64
@ cdecl _findfirst64(str ptr)
@ cdecl _findfirst64i32(str ptr)
@ cdecl _findnext32(long ptr)
@ stub _findnext32i64
@ cdecl _findnext64(long ptr)
@ cdecl _findnext64i32(long ptr)
@ cdecl _finite(double)
@ cdecl -arch=!i386 _finitef(float)
@ cdecl _flsbuf(long ptr)
@ cdecl _flushall()
@ extern _fmode MSVCRT__fmode
@ cdecl _fpclass(double)
@ cdecl -arch=!i386 _fpclassf(float)
@ cdecl -arch=i386,x86_64,arm,arm64 _fpieee_flt(long ptr ptr)
@ cdecl _fpreset()
@ stub _fprintf_l
@ stub _fprintf_p
@ stub _fprintf_p_l
@ stub _fprintf_s_l
@ cdecl _fputc_nolock(long ptr)
@ cdecl _fputchar(long)
@ cdecl _fputwc_nolock(long ptr)
@ cdecl _fputwchar(long)
@ cdecl _fread_nolock(ptr long long ptr)
@ cdecl _fread_nolock_s(ptr long long long ptr)
@ cdecl _free_locale(ptr)
@ stub _freea
@ stub _freea_s
@ stub _freefls
@ varargs _fscanf_l(ptr str ptr)
@ varargs _fscanf_s_l(ptr str ptr)
@ cdecl _fseek_nolock(ptr long long)
@ cdecl _fseeki64(ptr int64 long)
@ cdecl _fseeki64_nolock(ptr int64 long)
@ cdecl _fsopen(str str long)
@ cdecl _fstat32(long ptr)
@ cdecl _fstat32i64(long ptr)
@ cdecl _fstat64(long ptr)
@ cdecl _fstat64i32(long ptr)
@ cdecl _ftell_nolock(ptr)
@ cdecl -ret64 _ftelli64(ptr)
@ cdecl -ret64 _ftelli64_nolock(ptr)
@ cdecl _ftime32(ptr)
@ cdecl _ftime32_s(ptr)
@ cdecl _ftime64(ptr)
@ cdecl _ftime64_s(ptr)
@ cdecl -arch=i386 -ret64 _ftol()
@ cdecl _fullpath(ptr str long)
@ cdecl _futime32(long ptr)
@ cdecl _futime64(long ptr)
@ varargs _fwprintf_l(ptr wstr ptr)
@ stub _fwprintf_p
@ stub _fwprintf_p_l
@ stub _fwprintf_s_l
@ cdecl _fwrite_nolock(ptr long long ptr)
@ varargs _fwscanf_l(ptr wstr ptr)
@ varargs _fwscanf_s_l(ptr wstr ptr)
@ cdecl _gcvt(double long str)
@ cdecl _gcvt_s(ptr long double long)
@ cdecl _get_current_locale()
@ cdecl _get_daylight(ptr)
@ cdecl _get_doserrno(ptr)
@ cdecl _get_dstbias(ptr)
@ cdecl _get_errno(ptr)
@ cdecl _get_fmode(ptr)
@ cdecl _get_heap_handle()
@ cdecl _get_invalid_parameter_handler()
@ cdecl _get_osfhandle(long)
@ cdecl _get_output_format()
@ cdecl _get_pgmptr(ptr)
@ cdecl _get_printf_count_output()
@ cdecl _get_purecall_handler()
@ cdecl _get_terminate()
@ cdecl _get_timezone(ptr)
@ cdecl _get_tzname(ptr str long long)
@ cdecl _get_unexpected()
@ cdecl _get_wpgmptr(ptr)
@ cdecl _getc_nolock(ptr) _fgetc_nolock
@ cdecl _getch()
@ cdecl _getch_nolock()
@ cdecl _getche()
@ cdecl _getche_nolock()
@ cdecl _getcwd(str long)
@ cdecl _getdcwd(long str long)
@ stub _getdcwd_nolock
@ cdecl _getdiskfree(long ptr)
@ cdecl _getdllprocaddr(long str long)
@ cdecl _getdrive()
@ cdecl _getdrives() kernel32.GetLogicalDrives
@ cdecl _getmaxstdio()
@ cdecl _getmbcp()
@ cdecl _getpid()
@ cdecl _getptd()
@ stub _getsystime(ptr)
@ cdecl _getw(ptr)
@ cdecl _getwc_nolock(ptr) _fgetwc_nolock
@ cdecl _getwch()
@ cdecl _getwch_nolock()
@ cdecl _getwche()
@ cdecl _getwche_nolock()
@ cdecl _getws(ptr)
@ stub _getws_s
@ cdecl -arch=i386 _global_unwind2(ptr)
@ cdecl _gmtime32(ptr)
@ cdecl _gmtime32_s(ptr ptr)
@ cdecl _gmtime64(ptr)
@ cdecl _gmtime64_s(ptr ptr)
@ cdecl _heapadd(ptr long)
@ cdecl _heapchk()
@ cdecl _heapmin()
@ cdecl _heapset(long)
@ stub _heapused(ptr ptr)
@ cdecl _heapwalk(ptr)
@ cdecl _hypot(double double)
@ cdecl _hypotf(float float)
@ cdecl _i64toa(int64 ptr long)
@ cdecl _i64toa_s(int64 ptr long long)
@ cdecl _i64tow(int64 ptr long)
@ cdecl _i64tow_s(int64 ptr long long)
@ stub _initptd
@ cdecl _initterm(ptr ptr)
@ cdecl _initterm_e(ptr ptr)
@ stub -arch=i386 _inp(long)
@ stub -arch=i386 _inpd(long)
@ stub -arch=i386 _inpw(long)
@ cdecl _invalid_parameter(wstr wstr wstr long long)
@ cdecl _invalid_parameter_noinfo()
@ cdecl _invalid_parameter_noinfo_noreturn()
@ stub _invoke_watson
@ extern _iob MSVCRT__iob
@ cdecl _isalnum_l(long ptr)
@ cdecl _isalpha_l(long ptr)
@ cdecl _isatty(long)
@ cdecl _iscntrl_l(long ptr)
@ cdecl _isctype(long long)
@ cdecl _isctype_l(long long ptr)
@ cdecl _isdigit_l(long ptr)
@ cdecl _isgraph_l(long ptr)
@ cdecl _isleadbyte_l(long ptr)
@ cdecl _islower_l(long ptr)
@ stub _ismbbalnum(long)
@ stub _ismbbalnum_l
@ stub _ismbbalpha(long)
@ stub _ismbbalpha_l
@ stub _ismbbgraph(long)
@ stub _ismbbgraph_l
@ stub _ismbbkalnum(long)
@ stub _ismbbkalnum_l
@ cdecl _ismbbkana(long)
@ cdecl _ismbbkana_l(long ptr)
@ stub _ismbbkprint(long)
@ stub _ismbbkprint_l
@ stub _ismbbkpunct(long)
@ stub _ismbbkpunct_l
@ cdecl _ismbblead(long)
@ cdecl _ismbblead_l(long ptr)
@ stub _ismbbprint(long)
@ stub _ismbbprint_l
@ stub _ismbbpunct(long)
@ stub _ismbbpunct_l
@ cdecl _ismbbtrail(long)
@ cdecl _ismbbtrail_l(long ptr)
@ cdecl _ismbcalnum(long)
@ cdecl _ismbcalnum_l(long ptr)
@ cdecl _ismbcalpha(long)
@ cdecl _ismbcalpha_l(long ptr)
@ cdecl _ismbcdigit(long)
@ cdecl _ismbcdigit_l(long ptr)
@ cdecl _ismbcgraph(long)
@ cdecl _ismbcgraph_l(long ptr)
@ cdecl _ismbchira(long)
@ stub _ismbchira_l
@ cdecl _ismbckata(long)
@ stub _ismbckata_l
@ cdecl _ismbcl0(long)
@ cdecl _ismbcl0_l(long ptr)
@ cdecl _ismbcl1(long)
@ cdecl _ismbcl1_l(long ptr)
@ cdecl _ismbcl2(long)
@ cdecl _ismbcl2_l(long ptr)
@ cdecl _ismbclegal(long)
@ cdecl _ismbclegal_l(long ptr)
@ cdecl _ismbclower(long)
@ cdecl _ismbclower_l(long ptr)
@ cdecl _ismbcprint(long)
@ cdecl _ismbcprint_l(long ptr)
@ cdecl _ismbcpunct(long)
@ cdecl _ismbcpunct_l(long ptr)
@ cdecl _ismbcspace(long)
@ cdecl _ismbcspace_l(long ptr)
@ cdecl _ismbcsymbol(long)
@ stub _ismbcsymbol_l
@ cdecl _ismbcupper(long)
@ cdecl _ismbcupper_l(long ptr)
@ cdecl _ismbslead(ptr ptr)
@ stub _ismbslead_l
@ cdecl _ismbstrail(ptr ptr)
@ stub _ismbstrail_l
@ cdecl _isnan(double)
@ cdecl -arch=x86_64 _isnanf(float)
@ cdecl _isprint_l(long ptr)
@ cdecl _ispunct_l(long ptr)
@ cdecl _isspace_l(long ptr)
@ cdecl _isupper_l(long ptr)
@ cdecl _iswalnum_l(long ptr)
@ cdecl _iswalpha_l(long ptr)
@ cdecl _iswcntrl_l(long ptr)
@ stub _iswcsym_l
@ stub _iswcsymf_l
@ cdecl _iswctype_l(long long ptr)
@ cdecl _iswdigit_l(long ptr)
@ cdecl _iswgraph_l(long ptr)
@ cdecl _iswlower_l(long ptr)
@ cdecl _iswprint_l(long ptr)
@ cdecl _iswpunct_l(long ptr)
@ cdecl _iswspace_l(long ptr)
@ cdecl _iswupper_l(long ptr)
@ cdecl _iswxdigit_l(long ptr)
@ cdecl _isxdigit_l(long ptr)
@ cdecl _itoa(long ptr long)
@ cdecl _itoa_s(long ptr long long)
@ cdecl _itow(long ptr long)
@ cdecl _itow_s(long ptr long long)
@ cdecl _j0(double)
@ cdecl _j1(double)
@ cdecl _jn(long double)
@ cdecl _kbhit()
@ cdecl _lfind(ptr ptr ptr long ptr)
@ cdecl _lfind_s(ptr ptr ptr long ptr ptr)
@ cdecl _loaddll(str)
@ cdecl -arch=x86_64 _local_unwind(ptr ptr)
@ cdecl -arch=i386 _local_unwind2(ptr long)
@ cdecl -arch=i386 _local_unwind4(ptr ptr long)
@ cdecl _localtime32(ptr)
@ cdecl _localtime32_s(ptr ptr)
@ cdecl _localtime64(ptr)
@ cdecl _localtime64_s(ptr ptr)
@ cdecl _lock(long)
@ cdecl _lock_file(ptr)
@ cdecl _locking(long long long)
@ cdecl _logb(double)
@ cdecl -arch=!i386 _logbf(float)
@ cdecl -arch=i386 _longjmpex(ptr long) MSVCRT_longjmp
@ cdecl _lrotl(long long) MSVCRT__lrotl
@ cdecl _lrotr(long long) MSVCRT__lrotr
@ cdecl _lsearch(ptr ptr ptr long ptr)
@ stub _lsearch_s
@ cdecl _lseek(long long long)
@ cdecl -ret64 _lseeki64(long int64 long)
@ cdecl _ltoa(long ptr long)
@ cdecl _ltoa_s(long ptr long long)
@ cdecl _ltow(long ptr long)
@ cdecl _ltow_s(long ptr long long)
@ cdecl _makepath(ptr str str str str)
@ cdecl _makepath_s(ptr long str str str str)
@ cdecl _malloc_crt(long) malloc
@ cdecl _mbbtombc(long)
@ stub _mbbtombc_l
@ cdecl _mbbtype(long long)
@ cdecl _mbbtype_l(long long ptr)
# extern _mbcasemap
@ cdecl _mbccpy(ptr ptr)
@ cdecl _mbccpy_l(ptr ptr ptr)
@ cdecl _mbccpy_s(ptr long ptr ptr)
@ cdecl _mbccpy_s_l(ptr long ptr ptr ptr)
@ cdecl _mbcjistojms(long)
@ stub _mbcjistojms_l
@ cdecl _mbcjmstojis(long)
@ stub _mbcjmstojis_l
@ cdecl _mbclen(ptr)
@ stub _mbclen_l
@ cdecl _mbctohira(long)
@ stub _mbctohira_l
@ cdecl _mbctokata(long)
@ stub _mbctokata_l
@ cdecl _mbctolower(long)
@ stub _mbctolower_l
@ cdecl _mbctombb(long)
@ stub _mbctombb_l
@ cdecl _mbctoupper(long)
@ stub _mbctoupper_l
@ extern _mbctype MSVCRT_mbctype
@ stub _mblen_l
@ cdecl _mbsbtype(str long)
@ stub _mbsbtype_l
@ cdecl _mbscat_s(ptr long str)
@ cdecl _mbscat_s_l(ptr long str ptr)
@ cdecl _mbschr(str long)
@ stub _mbschr_l
@ cdecl _mbscmp(str str)
@ cdecl _mbscmp_l(str str ptr)
@ cdecl _mbscoll(str str)
@ cdecl _mbscoll_l(str str ptr)
@ cdecl _mbscpy_s(ptr long str)
@ cdecl _mbscpy_s_l(ptr long str ptr)
@ cdecl _mbscspn(str str)
@ cdecl _mbscspn_l(str str ptr)
@ cdecl _mbsdec(ptr ptr)
@ stub _mbsdec_l
@ cdecl _mbsicmp(str str)
@ stub _mbsicmp_l
@ cdecl _mbsicoll(str str)
@ cdecl _mbsicoll_l(str str ptr)
@ cdecl _mbsinc(str)
@ stub _mbsinc_l
@ cdecl _mbslen(str)
@ cdecl _mbslen_l(str ptr)
@ cdecl _mbslwr(str)
@ stub _mbslwr_l
@ cdecl _mbslwr_s(str long)
@ stub _mbslwr_s_l
@ cdecl _mbsnbcat(str str long)
@ stub _mbsnbcat_l
@ cdecl _mbsnbcat_s(str long ptr long)
@ stub _mbsnbcat_s_l
@ cdecl _mbsnbcmp(str str long)
@ stub _mbsnbcmp_l
@ cdecl _mbsnbcnt(ptr long)
@ stub _mbsnbcnt_l
@ cdecl _mbsnbcoll(str str long)
@ cdecl _mbsnbcoll_l(str str long ptr)
@ cdecl _mbsnbcpy(ptr str long)
@ stub _mbsnbcpy_l
@ cdecl _mbsnbcpy_s(ptr long str long)
@ cdecl _mbsnbcpy_s_l(ptr long str long ptr)
@ cdecl _mbsnbicmp(str str long)
@ stub _mbsnbicmp_l
@ cdecl _mbsnbicoll(str str long)
@ cdecl _mbsnbicoll_l(str str long ptr)
@ cdecl _mbsnbset(ptr long long)
@ stub _mbsnbset_l
@ stub _mbsnbset_s
@ stub _mbsnbset_s_l
@ cdecl _mbsncat(str str long)
@ stub _mbsncat_l
@ stub _mbsncat_s
@ stub _mbsncat_s_l
@ cdecl _mbsnccnt(str long)
@ stub _mbsnccnt_l
@ cdecl _mbsncmp(str str long)
@ stub _mbsncmp_l
@ stub _mbsncoll(str str long)
@ stub _mbsncoll_l
@ cdecl _mbsncpy(ptr str long)
@ stub _mbsncpy_l
@ stub _mbsncpy_s
@ stub _mbsncpy_s_l
@ cdecl _mbsnextc(str)
@ cdecl _mbsnextc_l(str ptr)
@ cdecl _mbsnicmp(str str long)
@ stub _mbsnicmp_l
@ stub _mbsnicoll(str str long)
@ stub _mbsnicoll_l
@ cdecl _mbsninc(str long)
@ stub _mbsninc_l
@ cdecl _mbsnlen(str long)
@ cdecl _mbsnlen_l(str long ptr)
@ cdecl _mbsnset(ptr long long)
@ stub _mbsnset_l
@ stub _mbsnset_s
@ stub _mbsnset_s_l
@ cdecl _mbspbrk(str str)
@ stub _mbspbrk_l
@ cdecl _mbsrchr(str long)
@ stub _mbsrchr_l
@ cdecl _mbsrev(str)
@ stub _mbsrev_l
@ cdecl _mbsset(ptr long)
@ stub _mbsset_l
@ stub _mbsset_s
@ stub _mbsset_s_l
@ cdecl _mbsspn(str str)
@ cdecl _mbsspn_l(str str ptr)
@ cdecl _mbsspnp(str str)
@ stub _mbsspnp_l
@ cdecl _mbsstr(str str)
@ stub _mbsstr_l
@ cdecl _mbstok(str str)
@ cdecl _mbstok_l(str str ptr)
@ cdecl _mbstok_s(str str ptr)
@ cdecl _mbstok_s_l(str str ptr ptr)
@ cdecl _mbstowcs_l(ptr str long ptr)
@ cdecl _mbstowcs_s_l(ptr ptr long str long ptr)
@ cdecl _mbstrlen(str)
@ cdecl _mbstrlen_l(str ptr)
@ stub _mbstrnlen
@ stub _mbstrnlen_l
@ cdecl _mbsupr(str)
@ stub _mbsupr_l
@ cdecl _mbsupr_s(str long)
@ stub _mbsupr_s_l
@ cdecl _mbtowc_l(ptr str long ptr)
@ cdecl _memccpy(ptr ptr long long)
@ cdecl _memicmp(str str long)
@ cdecl _memicmp_l(str str long ptr)
@ cdecl _mkdir(str)
@ cdecl _mkgmtime32(ptr)
@ cdecl _mkgmtime64(ptr)
@ cdecl _mktemp(str)
@ cdecl _mktemp_s(str long)
@ cdecl _mktime32(ptr)
@ cdecl _mktime64(ptr)
@ cdecl _msize(ptr)
@ cdecl _nextafter(double double)
@ cdecl -arch=x86_64 _nextafterf(float float)
@ cdecl _onexit(ptr)
@ varargs _open(str long)
@ cdecl _open_osfhandle(long long)
@ stub -arch=i386 _outp(long long)
@ stub -arch=i386 _outpd(long long)
@ stub -arch=i386 _outpw(long long)
@ cdecl _pclose(ptr)
@ extern _pctype MSVCRT__pctype
@ extern _pgmptr MSVCRT__pgmptr
@ cdecl _pipe(ptr long long)
@ cdecl _popen(str str)
@ stub _printf_l
@ stub _printf_p
@ stub _printf_p_l
@ stub _printf_s_l
@ cdecl _purecall()
@ cdecl _putc_nolock(long ptr) _fputc_nolock
@ cdecl _putch(long)
@ cdecl _putch_nolock(long)
@ cdecl _putenv(str)
@ cdecl _putenv_s(str str)
@ cdecl _putw(long ptr)
@ cdecl _putwc_nolock(long ptr) _fputwc_nolock
@ cdecl _putwch(long)
@ cdecl _putwch_nolock(long)
@ cdecl _putws(wstr)
@ extern _pwctype MSVCRT__pwctype
@ cdecl _read(long ptr long)
@ cdecl _realloc_crt(ptr long) realloc
@ cdecl _recalloc(ptr long long)
@ stub _recalloc_crt
@ cdecl _resetstkoflw()
@ cdecl _rmdir(str)
@ cdecl _rmtmp()
@ cdecl _rotl(long long) MSVCRT__rotl
@ cdecl -ret64 _rotl64(int64 long) MSVCRT__rotl64
@ cdecl _rotr(long long) MSVCRT__rotr
@ cdecl -ret64 _rotr64(int64 long) MSVCRT__rotr64
@ cdecl _scalb(double long)
@ cdecl -arch=x86_64 _scalbf(float long)
@ varargs _scanf_l(str ptr)
@ varargs _scanf_s_l(str ptr)
@ varargs _scprintf(str)
@ stub _scprintf_l
@ stub _scprintf_p
@ stub _scprintf_p_l
@ varargs _scwprintf(wstr)
@ stub _scwprintf_l
@ stub _scwprintf_p
@ stub _scwprintf_p_l
@ cdecl _searchenv(str str ptr)
@ cdecl _searchenv_s(str str ptr long)
@ stdcall -arch=i386 _seh_longjmp_unwind4(ptr)
@ stdcall -arch=i386 _seh_longjmp_unwind(ptr)
@ cdecl _set_SSE2_enable(long)
@ cdecl _set_abort_behavior(long long)
@ cdecl _set_controlfp(long long)
@ cdecl _set_doserrno(long)
@ cdecl _set_errno(long)
@ cdecl _set_error_mode(long)
@ cdecl _set_fmode(long)
@ cdecl _set_invalid_parameter_handler(ptr)
@ stub _set_malloc_crt_max_wait
@ cdecl _set_output_format(long)
@ cdecl _set_printf_count_output(long)
@ cdecl _set_purecall_handler(ptr)
@ cdecl _seterrormode(long)
@ cdecl -arch=i386,x86_64,arm,arm64 -norelay _setjmp(ptr) MSVCRT__setjmp
@ cdecl -arch=i386 -norelay _setjmp3(ptr long) MSVCRT__setjmp3
@ cdecl -arch=x86_64,arm -norelay _setjmpex(ptr ptr) __wine_setjmpex
@ cdecl _setmaxstdio(long)
@ cdecl _setmbcp(long)
@ cdecl _setmode(long long)
@ stub _setsystime(ptr long)
@ cdecl _sleep(long)
@ varargs _snprintf(ptr long str)
@ varargs _snprintf_c(ptr long str)
@ varargs _snprintf_c_l(ptr long str ptr)
@ varargs _snprintf_l(ptr long str ptr)
@ varargs _snprintf_s(ptr long long str)
@ varargs _snprintf_s_l(ptr long long str ptr)
@ varargs _snscanf(str long str)
@ varargs _snscanf_l(str long str ptr)
@ varargs _snscanf_s(str long str)
@ varargs _snscanf_s_l(str long str ptr)
@ varargs _snwprintf(ptr long wstr)
@ varargs _snwprintf_l(ptr long wstr ptr)
@ varargs _snwprintf_s(ptr long long wstr)
@ varargs _snwprintf_s_l(ptr long long wstr ptr)
@ varargs _snwscanf(wstr long wstr)
@ varargs _snwscanf_l(wstr long wstr ptr)
@ varargs _snwscanf_s(wstr long wstr)
@ varargs _snwscanf_s_l(wstr long wstr ptr)
@ varargs _sopen(str long long)
@ cdecl _sopen_s(ptr str long long long)
@ varargs _spawnl(long str str)
@ varargs _spawnle(long str str)
@ varargs _spawnlp(long str str)
@ varargs _spawnlpe(long str str)
@ cdecl _spawnv(long str ptr)
@ cdecl _spawnve(long str ptr ptr)
@ cdecl _spawnvp(long str ptr)
@ cdecl _spawnvpe(long str ptr ptr)
@ cdecl _splitpath(str ptr ptr ptr ptr)
@ cdecl _splitpath_s(str ptr long ptr long ptr long ptr long)
@ varargs _sprintf_l(ptr str ptr)
@ varargs _sprintf_p(ptr long str)
@ varargs _sprintf_p_l(ptr long str ptr)
@ varargs _sprintf_s_l(ptr long str ptr)
@ varargs _sscanf_l(str str ptr)
@ varargs _sscanf_s_l(str str ptr)
@ cdecl _stat32(str ptr)
@ cdecl _stat32i64(str ptr)
@ cdecl _stat64(str ptr)
@ cdecl _stat64i32(str ptr)
@ cdecl _statusfp()
@ cdecl -arch=i386 _statusfp2(ptr ptr)
@ cdecl _strcoll_l(str str ptr)
@ cdecl _strdate(ptr)
@ cdecl _strdate_s(ptr long)
@ cdecl _strdup(str)
@ cdecl _strerror(long)
@ cdecl _strerror_s(ptr long ptr)
@ cdecl _strftime_l(ptr long str ptr ptr)
@ cdecl _stricmp(str str)
@ cdecl _stricmp_l(str str ptr)
@ cdecl _stricoll(str str)
@ cdecl _stricoll_l(str str ptr)
@ cdecl _strlwr(str)
@ cdecl _strlwr_l(str ptr)
@ cdecl _strlwr_s(ptr long)
@ cdecl _strlwr_s_l(ptr long ptr)
@ cdecl _strncoll(str str long)
@ cdecl _strncoll_l(str str long ptr)
@ cdecl _strnicmp(str str long)
@ cdecl _strnicmp_l(str str long ptr)
@ cdecl _strnicoll(str str long)
@ cdecl _strnicoll_l(str str long ptr)
@ cdecl _strnset(str long long)
@ cdecl _strnset_s(str long long long)
@ cdecl _strrev(str)
@ cdecl _strset(str long)
@ stub _strset_s
@ cdecl _strtime(ptr)
@ cdecl _strtime_s(ptr long)
@ cdecl _strtod_l(str ptr ptr)
@ cdecl -ret64 _strtoi64(str ptr long)
@ cdecl -ret64 _strtoi64_l(str ptr long ptr)
@ cdecl _strtol_l(str ptr long ptr)
@ cdecl -ret64 _strtoui64(str ptr long)
@ cdecl -ret64 _strtoui64_l(str ptr long ptr)
@ cdecl _strtoul_l(str ptr long ptr)
@ cdecl _strupr(str)
@ cdecl _strupr_l(str ptr)
@ cdecl _strupr_s(str long)
@ cdecl _strupr_s_l(str long ptr)
@ cdecl _strxfrm_l(ptr str long ptr)
@ cdecl _swab(str str long)
@ varargs _swprintf(ptr wstr)
@ varargs _swprintf_c(ptr long str)
@ varargs _swprintf_c_l(ptr long str ptr)
@ stub _swprintf_p
@ varargs _swprintf_p_l(ptr long wstr ptr)
@ varargs _swprintf_s_l(ptr long wstr ptr)
@ varargs _swscanf_l(wstr wstr ptr)
@ varargs _swscanf_s_l(wstr wstr ptr)
@ extern _sys_errlist MSVCRT__sys_errlist
@ extern _sys_nerr MSVCRT__sys_nerr
@ cdecl _tell(long)
@ cdecl -ret64 _telli64(long)
@ cdecl _tempnam(str str)
@ cdecl _time32(ptr)
@ cdecl _time64(ptr)
@ extern _timezone MSVCRT___timezone
@ cdecl _tolower(long)
@ cdecl _tolower_l(long ptr)
@ cdecl _toupper(long)
@ cdecl _toupper_l(long ptr)
@ cdecl _towlower_l(long ptr)
@ cdecl _towupper_l(long ptr)
@ extern _tzname MSVCRT__tzname
@ cdecl _tzset()
@ cdecl _ui64toa(int64 ptr long)
@ cdecl _ui64toa_s(int64 ptr long long)
@ cdecl _ui64tow(int64 ptr long)
@ cdecl _ui64tow_s(int64 ptr long long)
@ cdecl _ultoa(long ptr long)
@ cdecl _ultoa_s(long ptr long long)
@ cdecl _ultow(long ptr long)
@ cdecl _ultow_s(long ptr long long)
@ cdecl _umask(long)
@ stub _umask_s
@ cdecl _ungetc_nolock(long ptr)
@ cdecl _ungetch(long)
@ cdecl _ungetch_nolock(long)
@ cdecl _ungetwc_nolock(long ptr)
@ cdecl _ungetwch(long)
@ cdecl _ungetwch_nolock(long)
@ cdecl _unlink(str)
@ cdecl _unloaddll(long)
@ cdecl _unlock(long)
@ cdecl _unlock_file(ptr)
@ cdecl _utime32(str ptr)
@ cdecl _utime64(str ptr)
@ cdecl _vcprintf(str ptr)
@ stub _vcprintf_l
@ stub _vcprintf_p
@ stub _vcprintf_p_l
@ stub _vcprintf_s
@ stub _vcprintf_s_l
@ cdecl _vcwprintf(wstr ptr)
@ stub _vcwprintf_l
@ stub _vcwprintf_p
@ stub _vcwprintf_p_l
@ stub _vcwprintf_s
@ stub _vcwprintf_s_l
@ cdecl _vfprintf_l(ptr str ptr ptr)
@ cdecl _vfprintf_p(ptr str ptr)
@ cdecl _vfprintf_p_l(ptr str ptr ptr)
@ cdecl _vfprintf_s_l(ptr str ptr ptr)
@ cdecl _vfwprintf_l(ptr wstr ptr ptr)
@ cdecl _vfwprintf_p(ptr wstr ptr)
@ cdecl _vfwprintf_p_l(ptr wstr ptr ptr)
@ cdecl _vfwprintf_s_l(ptr wstr ptr ptr)
@ stub _vprintf_l
@ stub _vprintf_p
@ stub _vprintf_p_l
@ stub _vprintf_s_l
@ cdecl _vscprintf(str ptr)
@ cdecl _vscprintf_l(str ptr ptr)
@ cdecl _vscprintf_p(str ptr)
@ cdecl _vscprintf_p_l(str ptr ptr)
@ cdecl _vscwprintf(wstr ptr)
@ cdecl _vscwprintf_l(wstr ptr ptr)
@ cdecl _vscwprintf_p(wstr ptr)
@ cdecl _vscwprintf_p_l(wstr ptr ptr)
@ cdecl -norelay _vsnprintf(ptr long str ptr)
@ cdecl _vsnprintf_c(ptr long str ptr)
@ cdecl _vsnprintf_c_l(ptr long str ptr ptr)
@ cdecl _vsnprintf_l(ptr long str ptr ptr)
@ cdecl _vsnprintf_s(ptr long long str ptr)
@ cdecl _vsnprintf_s_l(ptr long long str ptr ptr)
@ cdecl _vsnwprintf(ptr long wstr ptr)
@ cdecl _vsnwprintf_l(ptr long wstr ptr ptr)
@ cdecl _vsnwprintf_s(ptr long long wstr ptr)
@ cdecl _vsnwprintf_s_l(ptr long long wstr ptr ptr)
@ cdecl _vsprintf_l(ptr str ptr ptr)
@ cdecl _vsprintf_p(ptr long str ptr)
@ cdecl _vsprintf_p_l(ptr long str ptr ptr)
@ cdecl _vsprintf_s_l(ptr long str ptr ptr)
@ cdecl _vswprintf(ptr wstr ptr)
@ cdecl _vswprintf_c(ptr long wstr ptr)
@ cdecl _vswprintf_c_l(ptr long wstr ptr ptr)
@ cdecl _vswprintf_l(ptr wstr ptr ptr)
@ cdecl _vswprintf_p(ptr long wstr ptr)
@ cdecl _vswprintf_p_l(ptr long wstr ptr ptr)
@ cdecl _vswprintf_s_l(ptr long wstr ptr ptr)
@ stub _vwprintf_l
@ stub _vwprintf_p
@ stub _vwprintf_p_l
@ stub _vwprintf_s_l
@ cdecl _waccess(wstr long)
@ cdecl _waccess_s(wstr long)
@ cdecl _wasctime(ptr)
@ cdecl _wasctime_s(ptr long ptr)
@ cdecl _wassert(wstr wstr long)
@ cdecl _wchdir(wstr)
@ cdecl _wchmod(wstr long)
@ extern _wcmdln MSVCRT__wcmdln
@ cdecl _wcreat(wstr long)
@ cdecl _wcscoll_l(wstr wstr ptr)
@ cdecl _wcsdup(wstr)
@ cdecl _wcserror(long)
@ cdecl _wcserror_s(ptr long long)
@ cdecl _wcsftime_l(ptr long wstr ptr ptr)
@ cdecl _wcsicmp(wstr wstr)
@ cdecl _wcsicmp_l(wstr wstr ptr)
@ cdecl _wcsicoll(wstr wstr)
@ cdecl _wcsicoll_l(wstr wstr ptr)
@ cdecl _wcslwr(wstr)
@ cdecl _wcslwr_l(wstr ptr)
@ cdecl _wcslwr_s(wstr long)
@ cdecl _wcslwr_s_l(wstr long ptr)
@ cdecl _wcsncoll(wstr wstr long)
@ cdecl _wcsncoll_l(wstr wstr long ptr)
@ cdecl _wcsnicmp(wstr wstr long)
@ cdecl _wcsnicmp_l(wstr wstr long ptr)
@ cdecl _wcsnicoll(wstr wstr long)
@ cdecl _wcsnicoll_l(wstr wstr long ptr)
@ cdecl _wcsnset(wstr long long)
@ cdecl _wcsnset_s(wstr long long long)
@ cdecl _wcsrev(wstr)
@ cdecl _wcsset(wstr long)
@ cdecl _wcsset_s(wstr long long)
@ cdecl _wcstod_l(wstr ptr ptr)
@ cdecl -ret64 _wcstoi64(wstr ptr long)
@ cdecl -ret64 _wcstoi64_l(wstr ptr long ptr)
@ cdecl _wcstol_l(wstr ptr long ptr)
@ cdecl _wcstombs_l(ptr ptr long ptr)
@ cdecl _wcstombs_s_l(ptr ptr long wstr long ptr)
@ cdecl -ret64 _wcstoui64(wstr ptr long)
@ cdecl -ret64 _wcstoui64_l(wstr ptr long ptr)
@ cdecl _wcstoul_l(wstr ptr long ptr)
@ cdecl _wcsupr(wstr)
@ cdecl _wcsupr_l(wstr ptr)
@ cdecl _wcsupr_s(wstr long)
@ cdecl _wcsupr_s_l(wstr long ptr)
@ cdecl _wcsxfrm_l(ptr wstr long ptr)
@ cdecl _wctime32(ptr)
@ cdecl _wctime32_s(ptr long ptr)
@ cdecl _wctime64(ptr)
@ cdecl _wctime64_s(ptr long ptr)
@ cdecl _wctomb_l(ptr long ptr)
@ cdecl _wctomb_s_l(ptr ptr long long ptr)
@ extern _wctype MSVCRT__wctype
@ cdecl _wdupenv_s(ptr ptr wstr)
@ extern _wenviron MSVCRT__wenviron
@ varargs _wexecl(wstr wstr)
@ varargs _wexecle(wstr wstr)
@ varargs _wexeclp(wstr wstr)
@ varargs _wexeclpe(wstr wstr)
@ cdecl _wexecv(wstr ptr)
@ cdecl _wexecve(wstr ptr ptr)
@ cdecl _wexecvp(wstr ptr)
@ cdecl _wexecvpe(wstr ptr ptr)
@ cdecl _wfdopen(long wstr)
@ cdecl _wfindfirst32(wstr ptr)
@ stub _wfindfirst32i64
@ cdecl _wfindfirst64(wstr ptr)
@ cdecl _wfindfirst64i32(wstr ptr)
@ cdecl _wfindnext32(long ptr)
@ stub _wfindnext32i64
@ cdecl _wfindnext64(long ptr)
@ cdecl _wfindnext64i32(long ptr)
@ cdecl _wfopen(wstr wstr)
@ cdecl _wfopen_s(ptr wstr wstr)
@ cdecl _wfreopen(wstr wstr ptr)
@ cdecl _wfreopen_s(ptr wstr wstr ptr)
@ cdecl _wfsopen(wstr wstr long)
@ cdecl _wfullpath(ptr wstr long)
@ cdecl _wgetcwd(wstr long)
@ cdecl _wgetdcwd(long wstr long)
@ stub _wgetdcwd_nolock
@ cdecl _wgetenv(wstr)
@ cdecl _wgetenv_s(ptr ptr long wstr)
@ cdecl _wmakepath(ptr wstr wstr wstr wstr)
@ cdecl _wmakepath_s(ptr long wstr wstr wstr wstr)
@ cdecl _wmkdir(wstr)
@ cdecl _wmktemp(wstr)
@ cdecl _wmktemp_s(wstr long)
@ varargs _wopen(wstr long)
@ cdecl _wperror(wstr)
@ extern _wpgmptr MSVCRT__wpgmptr
@ cdecl _wpopen(wstr wstr)
@ stub _wprintf_l
@ stub _wprintf_p
@ stub _wprintf_p_l
@ stub _wprintf_s_l
@ cdecl _wputenv(wstr)
@ cdecl _wputenv_s(wstr wstr)
@ cdecl _wremove(wstr)
@ cdecl _wrename(wstr wstr)
@ cdecl _write(long ptr long)
@ cdecl _wrmdir(wstr)
@ varargs _wscanf_l(wstr ptr)
@ varargs _wscanf_s_l(wstr ptr)
@ cdecl _wsearchenv(wstr wstr ptr)
@ cdecl _wsearchenv_s(wstr wstr ptr long)
@ cdecl _wsetlocale(long wstr)
@ varargs _wsopen(wstr long long)
@ cdecl _wsopen_s(ptr wstr long long long)
@ varargs _wspawnl(long wstr wstr)
@ varargs _wspawnle(long wstr wstr)
@ varargs _wspawnlp(long wstr wstr)
@ varargs _wspawnlpe(long wstr wstr)
@ cdecl _wspawnv(long wstr ptr)
@ cdecl _wspawnve(long wstr ptr ptr)
@ cdecl _wspawnvp(long wstr ptr)
@ cdecl _wspawnvpe(long wstr ptr ptr)
@ cdecl _wsplitpath(wstr ptr ptr ptr ptr)
@ cdecl _wsplitpath_s(wstr ptr long ptr long ptr long ptr long)
@ cdecl _wstat32(wstr ptr)
@ cdecl _wstat32i64(wstr ptr)
@ cdecl _wstat64(wstr ptr)
@ cdecl _wstat64i32(wstr ptr)
@ cdecl _wstrdate(ptr)
@ cdecl _wstrdate_s(ptr long)
@ cdecl _wstrtime(ptr)
@ cdecl _wstrtime_s(ptr long)
@ cdecl _wsystem(wstr)
@ cdecl _wtempnam(wstr wstr)
@ cdecl _wtmpnam(ptr)
@ cdecl _wtmpnam_s(ptr long)
@ cdecl _wtof(wstr)
@ cdecl _wtof_l(wstr ptr)
@ cdecl _wtoi(wstr)
@ cdecl -ret64 _wtoi64(wstr)
@ cdecl -ret64 _wtoi64_l(wstr ptr)
@ cdecl _wtoi_l(wstr ptr)
@ cdecl _wtol(wstr)
@ cdecl _wtol_l(wstr ptr)
@ cdecl _wunlink(wstr)
@ cdecl _wutime32(wstr ptr)
@ cdecl _wutime64(wstr ptr)
@ cdecl _y0(double)
@ cdecl _y1(double)
@ cdecl _yn(long double)
@ cdecl abort()
@ cdecl abs(long)
@ cdecl acos(double)
@ cdecl -arch=!i386 acosf(float)
@ cdecl asctime(ptr)
@ cdecl asctime_s(ptr long ptr)
@ cdecl asin(double)
@ cdecl -arch=!i386 asinf(float)
@ cdecl atan(double)
@ cdecl -arch=!i386 atanf(float)
@ cdecl atan2(double double)
@ cdecl -arch=!i386 atan2f(float float)
@ cdecl -private atexit(ptr) MSVCRT_atexit  # not imported to avoid conflicts with Mingw
@ cdecl atof(str)
@ cdecl atoi(str)
@ cdecl atol(str)
@ cdecl bsearch(ptr ptr long long ptr)
@ cdecl bsearch_s(ptr ptr long long ptr ptr)
@ cdecl btowc(long)
@ cdecl calloc(long long)
@ cdecl ceil(double)
@ cdecl -arch=!i386 ceilf(float)
@ cdecl clearerr(ptr)
@ cdecl clearerr_s(ptr)
@ cdecl clock()
@ cdecl cos(double)
@ cdecl -arch=!i386 cosf(float)
@ cdecl cosh(double)
@ cdecl -arch=!i386 coshf(float)
@ cdecl -ret64 div(long long)
@ cdecl exit(long)
@ cdecl exp(double)
@ cdecl -arch=!i386 expf(float)
@ cdecl fabs(double)
@ cdecl fclose(ptr)
@ cdecl feof(ptr)
@ cdecl ferror(ptr)
@ cdecl fflush(ptr)
@ cdecl fgetc(ptr)
@ cdecl fgetpos(ptr ptr)
@ cdecl fgets(ptr long ptr)
@ cdecl fgetwc(ptr)
@ cdecl fgetws(ptr long ptr)
@ cdecl floor(double)
@ cdecl -arch=!i386 floorf(float)
@ cdecl fmod(double double)
@ cdecl -arch=!i386 fmodf(float float)
@ cdecl fopen(str str)
@ cdecl fopen_s(ptr str str)
@ varargs fprintf(ptr str)
@ varargs fprintf_s(ptr str)
@ cdecl fputc(long ptr)
@ cdecl fputs(str ptr)
@ cdecl fputwc(long ptr)
@ cdecl fputws(wstr ptr)
@ cdecl fread(ptr long long ptr)
@ cdecl fread_s(ptr long long long ptr)
@ cdecl free(ptr)
@ cdecl freopen(str str ptr)
@ cdecl freopen_s(ptr str str ptr)
@ cdecl frexp(double ptr)
@ varargs fscanf(ptr str)
@ varargs fscanf_s(ptr str)
@ cdecl fseek(ptr long long)
@ cdecl fsetpos(ptr ptr)
@ cdecl ftell(ptr)
@ varargs fwprintf(ptr wstr)
@ varargs fwprintf_s(ptr wstr)
@ cdecl fwrite(ptr long long ptr)
@ varargs fwscanf(ptr wstr)
@ varargs fwscanf_s(ptr wstr)
@ cdecl getc(ptr)
@ cdecl getchar()
@ cdecl getenv(str)
@ cdecl getenv_s(ptr ptr long str)
@ cdecl gets(str)
@ cdecl gets_s(ptr long)
@ cdecl getwc(ptr)
@ cdecl getwchar()
@ cdecl is_wctype(long long) iswctype
@ cdecl isalnum(long)
@ cdecl isalpha(long)
@ cdecl iscntrl(long)
@ cdecl isdigit(long)
@ cdecl isgraph(long)
@ cdecl isleadbyte(long)
@ cdecl islower(long)
@ cdecl isprint(long)
@ cdecl ispunct(long)
@ cdecl isspace(long)
@ cdecl isupper(long)
@ cdecl iswalnum(long)
@ cdecl iswalpha(long)
@ cdecl iswascii(long)
@ cdecl iswcntrl(long)
@ cdecl iswctype(long long)
@ cdecl iswdigit(long)
@ cdecl iswgraph(long)
@ cdecl iswlower(long)
@ cdecl iswprint(long)
@ cdecl iswpunct(long)
@ cdecl iswspace(long)
@ cdecl iswupper(long)
@ cdecl iswxdigit(long)
@ cdecl isxdigit(long)
@ cdecl labs(long)
@ cdecl ldexp(double long)
@ cdecl -ret64 ldiv(long long)
@ cdecl -ret64 llabs(int64)
@ cdecl -norelay lldiv(int64 int64)
@ cdecl localeconv()
@ cdecl log(double)
@ cdecl -arch=!i386 logf(float)
@ cdecl log10(double)
@ cdecl -arch=!i386 log10f(float)
@ cdecl -arch=i386,x86_64,arm,arm64 longjmp(ptr long) MSVCRT_longjmp
@ cdecl malloc(long)
@ cdecl mblen(ptr long)
@ cdecl mbrlen(ptr long ptr)
@ cdecl mbrtowc(ptr str long ptr)
@ cdecl mbsrtowcs(ptr ptr long ptr)
@ cdecl mbsrtowcs_s(ptr ptr long ptr long ptr)
@ cdecl mbstowcs(ptr str long)
@ cdecl mbstowcs_s(ptr ptr long str long) _mbstowcs_s
@ cdecl mbtowc(ptr str long)
@ cdecl memchr(ptr long long)
@ cdecl memcmp(ptr ptr long)
@ cdecl memcpy(ptr ptr long)
@ cdecl memcpy_s(ptr long ptr long)
@ cdecl memmove(ptr ptr long)
@ cdecl memmove_s(ptr long ptr long)
@ cdecl memset(ptr long long)
@ cdecl modf(double ptr)
@ cdecl -arch=!i386 modff(float ptr)
@ cdecl perror(str)
@ cdecl pow(double double)
@ cdecl -arch=!i386 powf(float float)
@ varargs printf(str)
@ varargs printf_s(str)
@ cdecl putc(long ptr)
@ cdecl putchar(long)
@ cdecl puts(str)
@ cdecl putwc(long ptr) fputwc
@ cdecl putwchar(long) _fputwchar
@ cdecl qsort(ptr long long ptr)
@ cdecl qsort_s(ptr long long ptr ptr)
@ cdecl raise(long)
@ cdecl rand()
@ cdecl rand_s(ptr)
@ cdecl realloc(ptr long)
@ cdecl remove(str)
@ cdecl rename(str str)
@ cdecl rewind(ptr)
@ varargs scanf(str)
@ varargs scanf_s(str)
@ cdecl setbuf(ptr ptr)
@ cdecl -arch=arm,x86_64 -norelay -private setjmp(ptr) MSVCRT__setjmp
@ cdecl setlocale(long str)
@ cdecl setvbuf(ptr str long long)
@ cdecl signal(long long)
@ cdecl sin(double)
@ cdecl -arch=!i386 sinf(float)
@ cdecl sinh(double)
@ cdecl -arch=!i386 sinhf(float)
@ varargs sprintf(ptr str)
@ varargs sprintf_s(ptr long str)
@ cdecl sqrt(double)
@ cdecl -arch=!i386 sqrtf(float)
@ cdecl srand(long)
@ varargs sscanf(str str)
@ varargs sscanf_s(str str)
@ cdecl strcat(str str)
@ cdecl strcat_s(str long str)
@ cdecl strchr(str long)
@ cdecl strcmp(str str)
@ cdecl strcoll(str str)
@ cdecl strcpy(ptr str)
@ cdecl strcpy_s(ptr long str)
@ cdecl strcspn(str str)
@ cdecl strerror(long)
@ cdecl strerror_s(ptr long long)
@ cdecl strftime(ptr long str ptr)
@ cdecl strlen(str)
@ cdecl strncat(str str long)
@ cdecl strncat_s(str long str long)
@ cdecl strncmp(str str long)
@ cdecl strncpy(ptr str long)
@ cdecl strncpy_s(ptr long str long)
@ cdecl strnlen(str long)
@ cdecl strpbrk(str str)
@ cdecl strrchr(str long)
@ cdecl strspn(str str)
@ cdecl strstr(str str)
@ cdecl strtod(str ptr)
@ cdecl strtok(str str)
@ cdecl strtok_s(ptr str ptr)
@ cdecl strtol(str ptr long)
@ cdecl strtoul(str ptr long)
@ cdecl strxfrm(ptr str long)
@ varargs swprintf_s(ptr long wstr)
@ varargs swscanf(wstr wstr)
@ varargs swscanf_s(wstr wstr)
@ cdecl system(str)
@ cdecl tan(double)
@ cdecl -arch=!i386 tanf(float)
@ cdecl tanh(double)
@ cdecl -arch=!i386 tanhf(float)
@ cdecl tmpfile()
@ cdecl tmpfile_s(ptr)
@ cdecl tmpnam(ptr)
@ cdecl tmpnam_s(ptr long)
@ cdecl tolower(long)
@ cdecl toupper(long)
@ cdecl towlower(long)
@ cdecl towupper(long)
@ cdecl ungetc(long ptr)
@ cdecl ungetwc(long ptr)
@ cdecl vfprintf(ptr str ptr)
@ cdecl vfprintf_s(ptr str ptr)
@ cdecl vfwprintf(ptr wstr ptr)
@ cdecl vfwprintf_s(ptr wstr ptr)
@ cdecl vprintf(str ptr)
@ cdecl vprintf_s(str ptr)
@ cdecl vsprintf(ptr str ptr)
@ cdecl vsprintf_s(ptr long str ptr)
@ cdecl vswprintf_s(ptr long wstr ptr)
@ cdecl vwprintf(wstr ptr)
@ cdecl vwprintf_s(wstr ptr)
@ cdecl wcrtomb(ptr long ptr)
@ cdecl wcrtomb_s(ptr ptr long long ptr)
@ cdecl wcscat(wstr wstr)
@ cdecl wcscat_s(wstr long wstr)
@ cdecl wcschr(wstr long)
@ cdecl wcscmp(wstr wstr)
@ cdecl wcscoll(wstr wstr)
@ cdecl wcscpy(ptr wstr)
@ cdecl wcscpy_s(ptr long wstr)
@ cdecl wcscspn(wstr wstr)
@ cdecl wcsftime(ptr long wstr ptr)
@ cdecl wcslen(wstr)
@ cdecl wcsncat(wstr wstr long)
@ cdecl wcsncat_s(wstr long wstr long)
@ cdecl wcsncmp(wstr wstr long)
@ cdecl wcsncpy(ptr wstr long)
@ cdecl wcsncpy_s(ptr long wstr long)
@ cdecl wcsnlen(wstr long)
@ cdecl wcspbrk(wstr wstr)
@ cdecl wcsrchr(wstr long)
@ cdecl wcsrtombs(ptr ptr long ptr)
@ cdecl wcsrtombs_s(ptr ptr long ptr long ptr)
@ cdecl wcsspn(wstr wstr)
@ cdecl wcsstr(wstr wstr)
@ cdecl wcstod(wstr ptr)
@ cdecl wcstok(wstr wstr)
@ cdecl wcstok_s(ptr wstr ptr)
@ cdecl wcstol(wstr ptr long)
@ cdecl wcstombs(ptr ptr long)
@ cdecl wcstombs_s(ptr ptr long wstr long)
@ cdecl wcstoul(wstr ptr long)
@ cdecl wcsxfrm(ptr wstr long)
@ cdecl wctob(long)
@ cdecl wctomb(ptr long)
@ cdecl wctomb_s(ptr ptr long long)
@ cdecl wmemcpy_s(ptr long ptr long)
@ cdecl wmemmove_s(ptr long ptr long)
@ varargs wprintf(wstr)
@ varargs wprintf_s(wstr)
@ varargs wscanf(wstr)
@ varargs wscanf_s(wstr)
